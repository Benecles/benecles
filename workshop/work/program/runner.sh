#!/bin/bash
# CUFRGS program runner (Claude, 2026-09-30). Zero-token manager: launches queued orders as FRESH Luna-high
# orchestrators, one at a time, checks each mechanically, retries once, sleeps through Codex 5h walls, stops near
# the weekly limit, and wakes the Luna-xhigh program manager (pm.md) whenever nothing is runnable.
P=/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program; W=/Users/benecles/Documents/Codex/2026-09-23/you-h/work
CODEX=/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex
MAXPM=${MAXPM:-10}; pm=0
log(){ echo "$(date '+%m-%d %H:%M') $*" >> $P/runner.log; }
st(){ cat $P/state/$1.status 2>/dev/null || echo pending; }
for pid in "$@"; do while ps -p $pid >/dev/null 2>&1; do sleep 30; done; done   # wait for runs started outside the queue
log "runner start (pid $$)"
LOCK_HEARTBEAT_PID=
lock_age(){
  stat -f %m "$1" 2>/dev/null || stat -c %Y "$1" 2>/dev/null || echo 0
}
lock_is_stale(){
  local path=$1 owner now mtime age cmd
  owner=$(cat "$path/pid" 2>/dev/null)
  now=$(date +%s); mtime=$(lock_age "$path"); age=$((now-mtime))
  if [[ "$owner" =~ ^[0-9]+$ ]]; then
    cmd=$(ps -p "$owner" -o command= 2>/dev/null)
    [[ "$cmd" == *"$P/runner.sh"* ]] || return 0
  fi
  (( age > 120 ))
}
lock_acquire(){
  local path=$1 stale
  until mkdir "$path" 2>/dev/null; do
    if [ -d "$path" ] && lock_is_stale "$path"; then
      local tombstone="$path.stale.$$"
      if mv "$path" "$tombstone" 2>/dev/null; then rm -rf "$tombstone"; fi
      continue
    fi
    sleep 2
  done
  printf '%s\n' "$$" > "$path/pid"
  ( while sleep 30; do
      local_cmd=$(ps -p "$$" -o command= 2>/dev/null)
      [[ "$local_cmd" == *"$P/runner.sh"* ]] || exit
      touch "$path" 2>/dev/null || exit
    done ) &
  LOCK_HEARTBEAT_PID=$!
}
lock_release(){
  local path=$1
  if [ -n "$LOCK_HEARTBEAT_PID" ]; then kill "$LOCK_HEARTBEAT_PID" 2>/dev/null || true; wait "$LOCK_HEARTBEAT_PID" 2>/dev/null || true; fi
  LOCK_HEARTBEAT_PID=
  rm -f "$path/pid"
  rmdir "$path" 2>/dev/null || true
}
gate(){ while true; do g=$(python3 $P/usage_gate.py); case $g in ok) return 0;; stop) log "weekly Codex limit nearly used: stopping"; exit 0;; sleep*) s=${g#sleep }; log "5h window full: sleeping ${s}s"; sleep $s;; esac; done; }
next(){ today=$(date +%F)
  busy=$(grep -v '^#' $P/queue.tsv | while IFS=$'\t' read -r i a n c l; do [ "$(st $i)" = running ] && [ -n "$l" ] && [ "$l" != "-" ] && echo "$l"; done)
  grep -v '^#' $P/queue.tsv | while IFS=$'\t' read -r id after nb chk lock; do
    [ -z "$id" ] && continue; s=$(st $id)
    case $s in done|blocked|running|"failed 2") continue;; esac
    [ "$nb" != "-" ] && [[ "$today" < "$nb" ]] && continue
    [ -n "$lock" ] && [ "$lock" != "-" ] && echo "$busy" | grep -qx "$lock" && continue
    ok=1; if [ "$after" != "-" ]; then
      for d in ${after//,/ }; do
        case "$d" in ship:*) [ -f "$P/ships/done/${d#ship:}.md" ] || ok=0;; *) [ "$(st $d)" = done ] || ok=0;; esac
      done
    fi
    [ $ok = 1 ] && { echo "$id"; break; }
  done; }
pick(){ lock_acquire "$P/.pick"; id=$(next); if [ -n "$id" ]; then st $id > $P/state/$id.prev; echo running > $P/state/$id.status; fi; lock_release "$P/.pick"; }
while true; do
  pick
  if [ -z "$id" ]; then
    head -1 $P/claude-inbox.md 2>/dev/null | grep -q '^DONE' && { log "PM says DONE: exiting"; exit 0; }
    # only dated items waiting? sleep an hour and look again (no PM call needed)
    if grep -v '^#' $P/queue.tsv | awk -F'\t' '$3!="-"' | while IFS=$'\t' read -r i a nb c; do [ "$(st $i)" = pending ] && echo x; done | grep -q x && [ $pm -ge $MAXPM ]; then sleep 3600; continue; fi
    [ $pm -ge $MAXPM ] && { log "PM cap reached: exiting"; exit 0; }
    if [ -f $P/.pm_last ] && [ $(( $(date +%s) - $(stat -f %m $P/.pm_last) )) -lt 1800 ]; then sleep 300; continue; fi  # PM cooldown (30/09): one PM run per 30 min across all runners
    lock_acquire "$P/.pm"; touch $P/.pm_last
    gate; pm=$((pm+1)); log "PM run $pm ($$)"
    $CODEX exec -m gpt-6-luna -c model_reasoning_effort=xhigh --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check -C $W -o $P/logs/pm-$$-$pm.last.txt "$(cat $P/pm.md)" < /dev/null > $P/logs/pm-$$-$pm.log 2>&1
    log "PM run $pm: $(head -c 300 $P/logs/pm-$$-$pm.last.txt | tr '\n' ' ')"; lock_release "$P/.pm"
    [ -z "$(next)" ] && sleep 60
    continue
  fi
  s=$(cat $P/state/$id.prev 2>/dev/null); rm -f $P/state/$id.prev; n=1; [ "$s" = "failed 1" ] && n=2
  chk=$(grep -v '^#' $P/queue.tsv | awk -F'\t' -v i="$id" '$1==i{print $4}')
  of=$P/orders/$id.md; [ -f $of ] || { log "$id: no order file"; echo blocked > $P/state/$id.status; continue; }
  gate; log "$id attempt $n: launching"
  extra=""; [ $n = 2 ] && extra=$'\n\nPREVIOUS ATTEMPT FAILED ITS CHECK. Check output (tail):\n'"$(tail -30 $P/logs/$id.check.txt 2>/dev/null)"$'\nInspect the current state, keep what holds up, and fix what the check reports.'
  $CODEX exec -m gpt-6-luna -c model_reasoning_effort=high --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check -C $W -o $P/logs/$id.a$n.last.txt "$(cat $P/preamble.md $of)$extra" < /dev/null > $P/logs/$id.a$n.log 2>&1
  (cd $W && bash -c "$chk") > $P/logs/$id.check.txt 2>&1; rc=$?
  if [ $rc = 0 ]; then
    echo done > $P/state/$id.status; log "$id: DONE (check passed)"
    python3 "$P/ships/shipper.py" prepare "$id" >> "$P/logs/$id.ship.log" 2>&1 || log "$id: ship request preparation needs attention"
  elif grep -qi 'usage limit' "$P/logs/$id.a$n.log" || [ "$(python3 "$P/usage_gate.py")" != "ok" ]; then
    echo pending > $P/state/$id.status; [ $n = 2 ] && echo "failed 1" > $P/state/$id.status
    log "$id: usage limit found in the explicit error or rate_limits state; will retry when allowed"
  else echo "failed $n" > $P/state/$id.status; log "$id: check FAILED (attempt $n)"; fi
done

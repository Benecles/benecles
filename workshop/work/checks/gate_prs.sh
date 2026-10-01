#!/bin/bash
# Gate site PRs before merging: runs svgcheck on every changed page of each PR.
# On PASS it writes a stamp the chair mod reads before allowing `gh pr merge`:
#   ~/.cache/ordenacoes-gate/pr-<N>  (contents: the PR head SHA that was checked)
# Usage: work/checks/gate_prs.sh 41 42 ...     (any cwd)
set -u
SITE=~/Developer/ordenacoes-filipinas
HERE="$(cd "$(dirname "$0")" && pwd)"
STAMPS=~/.cache/ordenacoes-gate
mkdir -p "$STAMPS"
cd "$SITE" || exit 2
git fetch -q origin
status=0
for n in "$@"; do
  branch=$(gh pr view "$n" --json headRefName --jq .headRefName) || { echo "PR $n: not found"; status=1; continue; }
  sha=$(gh pr view "$n" --json headRefOid --jq .headRefOid)
  git fetch -q origin "$branch"
  pages=()
  while IFS= read -r f; do pages+=("$f"); done < <(gh pr view "$n" --json files --jq '.files[].path' | grep -E '\.html$' | grep -v '^polish/')
  echo "== PR $n ($branch) · ${#pages[@]} pages"
  if [ ${#pages[@]} -eq 0 ] || python3 "$HERE/svgcheck.py" "origin/$branch" "${pages[@]}"; then
    echo "$sha" > "$STAMPS/pr-$n"; echo "PR $n: PASS (stamped)"
  else
    rm -f "$STAMPS/pr-$n"; echo "PR $n: FAIL"; status=1
  fi
done
exit $status

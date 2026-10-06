#!/bin/bash
# Usage (from site repo, on a feature branch with edits made): ship.sh "TITLE" "ISSUES line body"
# site-edit procedure -> commit -> push -> PR -> wait for CI -> merge. No attribution lines (chairman, 06/10).
set -e
T="$1"; L="$2"
python3 tools/offline_build.py | tail -1
git checkout -- assets/front.css specimen/register.html
python3 tools/polish.py capture | tail -1
rm -rf tools/polish/specimen
git add -A courses assets tools offline-manifest.json specimen
printf -- '- **%s** · %s\n' "$T" "$L" >> ISSUES.md
git add ISSUES.md
bash tools/check_all.sh | tail -1
git add -A courses assets tools offline-manifest.json specimen ISSUES.md
python3 tools/offline_build.py >/dev/null; git checkout -- assets/front.css specimen/register.html; git add -A offline-manifest.json
bash tools/check_all.sh | tail -1 | grep -q PASS
git commit -qm "$T"
B=$(git branch --show-current)
git push -q -u origin "$B"
N=$(gh pr create --title "$T" --body "$L" | grep -o '[0-9]*$')
for i in $(seq 1 20); do sleep 10; r=$(gh pr checks $N 2>/dev/null | awk '{print $2}' | head -1); [ "$r" = pass ] && break; [ "$r" = fail ] && { echo "CI FAIL on #$N"; exit 1; }; done
gh pr merge $N --merge | tail -1
git checkout -q main; git pull -q
echo "merged #$N"

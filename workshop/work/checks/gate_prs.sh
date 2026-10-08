#!/bin/bash
# Gate site PRs before merging: runs svgcheck on every changed page of each PR.
# Usage: work/checks/gate_prs.sh 41 42 ...     (any cwd)
set -u
SITE=~/Developer/ordenacoes-filipinas
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$SITE" || exit 2
git fetch -q origin
status=0
for n in "$@"; do
  branch=$(gh pr view "$n" --json headRefName --jq .headRefName) || { echo "PR $n: not found"; status=1; continue; }
  git fetch -q origin "$branch"
  pages=()
  while IFS= read -r f; do pages+=("$f"); done < <(gh pr view "$n" --json files --jq '.files[].path' | grep -E '\.html$' | grep -v '^polish/')
  echo "== PR $n ($branch) · ${#pages[@]} pages"
  if [ ${#pages[@]} -eq 0 ] || python3 "$HERE/svgcheck.py" "origin/$branch" "${pages[@]}"; then
    echo "PR $n: PASS"
  else
    echo "PR $n: FAIL"; status=1
  fi
done
exit $status

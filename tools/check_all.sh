#!/bin/sh
# Cheap site-wide checks. Run from anywhere; exits non-zero on any FAIL.
# 1. Fronts are reproducible: regenerating from tools/fronts/data must not change committed courses/*/index.html.
# 2. check_front: macro order, dead/missing lesson links, bibliografia.
cd "$(dirname "$0")/.." || exit 2
slugs=$(ls tools/fronts/data | sed 's/\.json$//')
python3 tools/fronts/front.py $slugs >/dev/null && python3 -c "import sys; sys.path.insert(0, 'tools'); import assetver; assetver.run()" >/dev/null || exit 1
fail=0
for s in $slugs; do
  if ! git diff --quiet -- "courses/$s/index.html"; then
    echo "FAIL $s: regenerated front differs from committed (data out of sync with live; see git diff)"; fail=1
  fi
done
python3 tools/fronts/check_front.py $slugs | grep -v '^WARN' || fail=1
[ $fail = 0 ] && echo "check_all: PASS" || echo "check_all: FAIL"
exit $fail

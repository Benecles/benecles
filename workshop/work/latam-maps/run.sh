#!/bin/zsh
# Latam maps pass (Claude, 05/10): rebuild front, A01 and A02 map fixes from origin/main in a site checkout.
# usage: run.sh SITE_CHECKOUT
set -e
SITE=$1; HERE=${0:a:h}; L=courses/direito-latino-americano
cd $SITE
git checkout origin/main -- $L/aula-01.html $L/aula-02.html $L/index.html tools/fronts/data/direito-latino-americano.json
python3 $HERE/apply_labels.py $L/aula-01.html '<svg class="hero-fork hero-map"' $HERE/a01_hero.json --join-routes
python3 $HERE/a01_crisis.py $L/aula-01.html
python3 $HERE/a02_atlas.py $L/aula-02.html
(cd $HERE/../latam-build && PYTHONPATH=../contract-build/generators python3 front_courts.py $SITE/tools/fronts/data/direito-latino-americano.json)
python3 tools/fronts/front.py direito-latino-americano

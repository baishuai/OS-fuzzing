#!/usr/bin/env bash
for seed in $(seq 0 2); do
  python split.py $1 $seed
  vpredictor --out-file data/$seed/zzuf.pklz --train --dynamic data/$seed/train.csv > /dev/null
  vpredictor --test --model data/$seed/zzuf.pklz --dynamic data/$seed/test.csv --out-file data/$seed/pred.csv
done

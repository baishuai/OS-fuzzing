#!/bin/sh


if [ $# -ne 2 ]; then
    # TODO: print usage
    echo xxx
    exit 1
fi

OUTPUTERR=$1.err
OUTPUT=$1.out

printf "" > $OUTPUTERR
#printf "" > $OUTPUT

for testcase in $(ls "$1" | shuf); do
  time  -f "$testcase\t%E\t%x" ./VDiscover/vdp --io-mode --seed-range "0:1000" "$1/$testcase" "$2" 2>> $OUTPUTERR > /dev/null #$OUTPUT
done

# ./get_crashes.sh ./zzuf_testcases "zzuf -r0.005:0.05 -s <seed> < <input> > <output>"

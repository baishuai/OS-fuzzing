#!/bin/sh


if [ $# -ne 1 ]; then
    # TODO: print usage
    echo xxx
    exit 1
fi

OUTPUTERR=$1.err
OUTPUT=$1.out

printf "" > $OUTPUTERR
#printf "" > $OUTPUT

for testcase in $(ls "$1" | shuf); do
  echo $testcase
  # _usr_bin_foo2hiperc:20476
  cmd=$(echo $testcase | cut -d '_' -f4 | cut -d ':' -f1)
  echo $cmd
  time --quiet -f "$testcase\t%E\t%x" vdp "$1/$testcase" "$cmd" 2>> $OUTPUTERR > /dev/null #$OUTPUT
done


#!/bin/bash
inputfile="$1"
dups=0
while read count subj_acc
do
    if [ "$count" -ge 2 ]; then
        dups=$((dups+1))
    fi
done < <(tail -n +6 "$inputfile" | cut -f2 | sort | uniq -c)
echo "There are ${dups} subject sequences with more than one HSP"

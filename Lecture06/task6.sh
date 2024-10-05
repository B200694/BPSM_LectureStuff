#!/bin/bash
inputfile="$1"
count=0
while read query_acc subj_acc perc_id align_length mismatches gap_opens q_start q_end s_start s_end e_value bit_score
do
	if [ ${align_length} -lt 100 ]; then
		count=$((count+1))
	fi
done < <(tail -n +6 "$inputfile")
echo "There are ${count} HSPs shorter than 100 amino acids"

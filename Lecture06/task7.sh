#!/bin/bash
inputfile="$1"
echo "Top 10 HSPs by bit score:"
count=0
echo -e "subj_acc\tbit_score"
while read query_acc subj_acc perc_id align_length mismatches gap_opens q_start q_end s_start s_end e_value bit_score
do
	echo -e "${subj_acc}\t${bit_score}"
	count=$((count+1))
	if [ ${count} -eq 10 ]; then
		break
	fi
done < <(tail -n +6 "$inputfile")

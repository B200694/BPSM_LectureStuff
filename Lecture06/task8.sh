#!/bin/bash
inputfile="$1"
echo "Start positions of all matches with subject accession AEI"
echo -e "subj_acc\tq_start\ts_start"
while read query_acc subj_acc perc_id align_length mismatches gap_opens q_start q_end s_start s_end e_value bit_score
do
	if [[ ${subj_acc} == *"AEI"* ]]; then
		echo -e "${subj_acc}\t${q_start}\t${s_start}"
	fi
done < <(tail -n +6 "$inputfile")

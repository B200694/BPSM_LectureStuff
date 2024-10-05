#!/bin/bash
inputfile="$1"
echo "List of HSPs with more than 20 mismatches:"
echo -e "subj_acc\tmismatches"
tail -n +6 "$inputfile" | while read query_acc subj_acc perc_id align_length mismatches gap_opens q_start q_end s_start s_end e_value bit_score
do
	if [ ${mismatches} -gt 20 ];
	then
		echo -e "${subj_acc}\t${mismatches}"
	fi
done

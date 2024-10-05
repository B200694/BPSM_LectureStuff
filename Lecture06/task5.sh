#!/bin/bash
inputfile="$1"
echo "First 20 HSPs with less than 20 mismatches:"
echo -e "number\tsubj_acc\tmismatches"
count=0
tail -n +6 "$inputfile" | while read query_acc subj_acc perc_id align_length mismatches gap_opens q_start q_end s_start s_end e_value bit_score
do
	if [ ${mismatches} -lt 20 ]; then
                count=$((count+1))
		echo -e "${count}\t${subj_acc}\t${mismatches}"
        fi
	if [ ${count} -eq 20 ]; then
		break
	fi
done

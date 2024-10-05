#!/bin/bash
inputfile="$1"
echo -e "What percentage of each HSP is made up of mismatches?"
echo -e "subj_acc\talign_length\tmismatches\tMMpercent"
while read query_acc subj_acc perc_id align_length mismatches gap_opens q_start q_end s_start s_end e_value bit_score
do
	MMpercent=$(( 100 * ${mismatches} / ${align_length} ))
	echo -e "${subj_acc}\t${align_length}\t${mismatches}\t${MMpercent}"
done < <(tail -n +6 "$inputfile")

#!/bin/bash
inputfile="$1"
echo -e "Listing all subject accessions, alignment lengths & percent IDs:"
echo -e "subj_acc\talign_length\tperc_id"
tail -n +6 "$inputfile" | while read query_acc subj_acc perc_id align_length mismatches gap_opens q_start q_end s_start s_end e_value bit_score
do
echo -e "${subj_acc}\t${align_length}\t${perc_id}"
done

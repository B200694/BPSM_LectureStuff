#!/bin/bash
inputfile="$1"
group1cut=150
group2cut=250
group3cut=350
outfile1="HSPscore_under_${group1cut}.out"
outfile2="HSPscore_${group1cut}_to_${group2cut}.out"
outfile3="HSPscore_${group2cut}_to_${group3cut}.out"
outfile4="HSPscore_over_${group3cut}.out"
while read query_acc subj_acc perc_id align_length mismatches gap_opens q_start q_end s_start s_end e_value bit_score
do
scorebin=1
	if [ ${bit_score} -gt ${group3cut} ]; then
     		scorebin=4
	fi
	if [ ${bit_score} -le ${group3cut} ] && [ ${bit_score} -gt ${group2cut} ]; then
     		scorebin=3
	fi
	if [ ${bit_score} -le ${group2cut} ] && [ ${bit_score} -gt ${group1cut} ]; then
     		scorebin=2
	fi
	scoregroupdetails=$(echo -e "${subj_acc}\t${query_acc}\t${subj_acc}\t${bit_score}")
	case $scorebin in
  		4)
    			echo -e "${scoregroupdetails}" >> ${outfile4}
    			;;
  		3)
    			echo -e "${scoregroupdetails}" >> ${outfile3}
    			;;
  		2)
    			echo -e "${scoregroupdetails}" >> ${outfile2}
    			;;
  		1)
    			echo -e "${scoregroupdetails}" >> ${outfile1}
   	 		;;
	esac
done < <(tail -n +6 "$inputfile")

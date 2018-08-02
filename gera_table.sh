#!/bin/bash


# This script gets all images with .gif extension at argument directory. The files must be named as ana_iagAAMMDDHHMMSSSS.gif.
# Inputs: Calls gera_table.tex IMAGEDIR
# Outputs: Creates files named as MMDD.tex filled with Latex code for tables. At the current version, it allows 2 images per page inside each \begin{figure} statement.

cd $1
rm *tex*
year=`ls *gif | head -1 | cut -c 8-9 | uniq`
month=`ls *gif | head -1 | cut -c 10-11 | uniq`
count=0

for i in ` ls *gif | cut -c 12-13 | uniq`; do
	echo "Header"
	echo "\begin{figure*}[!htb]" >> $month$i.tex
	echo "\centerline{" >> $month$i.tex
	for j in `ls ana_iag$year$month$i*.gif`; do
		count=`expr $count + 1`
		if [ $count -eq 3 ] ; then
			echo $count
			echo "}" >> $month$i.tex
			echo "\label{}" >> $month$i.tex
			echo "\end{figure*}" >> $month$i.tex
			echo >> $month$i.tex
			echo "\begin{figure*}[!htb]" >> $month$i.tex
			echo "\centerline{" >> $month$i.tex
			count=0
			echo $count
		fi;
		echo "\subfigure[]{\includegraphics[scale=0.3]{$j}" >> 	$month$i.tex
		echo "\label{fig}}" >> $month$i.tex
		echo "\hfil" >> $month$i.tex
	done;
	echo "}" >> $month$i.tex
	echo "\caption{Images from $year / $month / $i }" >> $month$i.tex
	echo "\label{}" >> $month$i.tex
	echo "\end{figure*}" >> $month$i.tex
done
cd ..


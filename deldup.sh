#!/bin/bash

#This script must be run in the directory you specified in selchrome.py
#on line 12.  This deletes any duplicate songs and replaces spaces in file names with -

for filename in *.mp3
do
	new=${filename//[ ]/-}
	new=${new//[\',+()\]\[124567890&]/}
	new=${new//---/-}
	new=${new//--/-}
	new=${new//-./.}
	if [ "$filename" != "$new" ]
	then
		mv "$filename" "$new"
	fi
done

cksum  *.mp3 | sort -n > filelist
old=""
while read sum lines filename || [[ -n $one ]]
do
	if [[ "$sum" != "$old" ]]
	then
		old="$sum"
		continue
	fi
	echo "removing  $filename"
	rm -f "$filename"
done <filelist

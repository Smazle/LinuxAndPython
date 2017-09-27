#Get Smallest Value in second column
sort -u -k 2,2 experimental_results.txt | head -1 | cut -d\  -f2

#Use Xargs and du, to sort a list files from smallest to largest
find /usr/share/dict -type f | xargs du -h | sort -h -k 1 | cut -f2

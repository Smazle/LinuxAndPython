# 1. Edjucational background
echo "Computer Science" > background.txt

# 2. Search for file based in /usr/, starting with th_en_US, and ending in .dat
result=$(find /usr/ | grep '.dat$' | grep 'th_en_US')
echo result

# 3. Get lines with the word hacker 
cat $result | grep "hacker" 

# 4. Get 3 + lines starting with "("
$result | grep "hacker" | grep "^("



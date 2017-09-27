# 1. Edjucational background
echo "Computer Science" > background.txt

# 2. Search for file based in /usr/, starting with th_en_US, and ending in .dat
result=$(find /usr/ | grep '.dat$' | grep 'th_en_US')
echo $result

# 3. Get lines with the word hacker 
cat $result | grep "hacker" 

# 4. Pev + first char being "("
cat $result | grep "hacker" | grep "^("

# 5. All prev + only the first output
cat $result | grep "hacker" | grep -m 1 "^(" 

# 6. Replace '|' with '\n'
cat $result | grep "hacker" | grep -m 1 "^(" | tr '|' '\n'

# 7. Dont output first line
cat $result | grep "hacker" | grep -m 1 "^(" | tr '|' '\n' | tail -n +2

# 8. Print the line numbers
cat $result | grep "hacker" | grep -m 1 "^(" | tr '|' '\n' | tail -n +2 | nl

# 9. Save output to file
cat $result | grep "hacker" | grep -m 1 "^(" | tr '|' '\n' | tail -n +2 | nl > hacker_output.txt

# 10. Download file
wget "http://people.binf.ku.dk/wb/lpp2017/week37/nix_script.sh"

# 11. Make the file executale
chmod +x nix_script.sh

# 12. Run file
./nix_script.sh

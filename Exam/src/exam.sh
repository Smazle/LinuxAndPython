#Bash Script

# Uses regex [a-zA-Z; .] to count lines starting with a letter
grep -c '^[a-zA-Z; .]' "data/countries.dat"


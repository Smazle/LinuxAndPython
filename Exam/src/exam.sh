# Task 1.3 Uses regex [a-zA-Z; .] to count lines starting with a letter
# Instead of negating the regex used, in 1.1, i made my own.
grep -c '^[a-zA-Z; .]' "data/countries.dat"

# Task 2.4 Uses convert with loop set to 0, and delay between images set to 75
convert -loop 0 -delay 75 globe_map_0* globe_map_animated.gif

# Task 3.3 - First extract the columns of intrerest, and then uses a series of
# regex replacements to get the data i want. The headers are excluded as well.
# Currently the result is delimited by ";", but could simply be replaced with 
# tabs using sed -e "s/\;/\t/g" if required.
cat ./data/north_korea_missile_test_database.csv | cut -d ";" -f 10,11,14 | sed -e "s/\,/\./g" -e "s/\ km//g" | grep -E "(([0-9]+\.[0-9]+;){2}([0-9]+))" > north_korea_missile_test_database_filtered.csv


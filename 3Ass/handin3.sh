# Compress file and preserve orignal
bzip2 -k "./experimental_results.txt"

# Print out file sizes of before and after compression
ls -la experimental_results.txt* | tr -s ' ' '\t' | cut -f5

# Replace all digits in file by 0
tr [:digit:] '0' < experimental_results.txt > experimental_results_zeros.txt

# Output their size
ls -la experimental_results*.txt | tr -s ' ' '\t' | cut -f5

# Compress the zeroed out file, and print out its' size and original size
bzip2 -k "./experimental_results_zeros.txt"
ls -la experimental_results_zeros* | tr -s ' ' '\t' | cut -f5

# use echo and tee to write the explanation both to a file called "explanation.txt" and to stdout.
STR="It uses run-length encoding, which is where a numeric value is used to represented repetetions in the file.
If the file contains the sequence \"WWWW\" this can be represented as \"4W\" after
compression, resulting in reduced file size, and easy reverseability."
echo $STR | tee explanation.txt


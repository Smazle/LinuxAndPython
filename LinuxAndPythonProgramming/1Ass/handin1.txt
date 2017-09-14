# 1. Create directory
mkdir handin1

# 2. Inside prev directory make another directory
mkdir handin1/test1/

# 3. Download file and place into newly created directory
wget http://people.binf.ku.dk/wb/data/m_scrambled.txt -P ./handin1/test1/

# 4. Copy folder
cp -r ./handin1/test1/ ./handin1/test2/

# 5. Move to and output content of handin1 folder
cd ./handin1/
find . -print

# 6. Delete test2 folder
rm -rf ./test2/

# 7. Show content of file downloaded
cat ./test1/m_scrambled.txt

# 8. Unscramble file
sort -k 1 -n ./test1/m_scrambled.txt > ./test1/m.txt

# 9. Wget and rename
wget -O - http://people.binf.ku.dk/wb/data/m_scrambled.txt | sort -k 1 -n > ./test1/m.txt

# 10. Delete the handin1 folder
rm -rf ../handin1/

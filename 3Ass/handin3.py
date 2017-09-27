lines = open("./11-0.txt").readlines()

print(len(lines))

print(lines[40])

print(len(lines[42].split(" ")))

junk_file = open('junk.txt', 'w')
junk_file.writelines(lines[8:11])
junk_file.close()

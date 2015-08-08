fi = open('sample.txt', 'r')
for line in fi:
    line = line.rstrip()
    if line == "Education":
        print line

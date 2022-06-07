f = open('file.txt')

while True:
    line = f.readline()
    if not line:
        break
    # print(line, end='')
    # sau
    line_new = line.strip('\n')
    print(line_new)
f.close()

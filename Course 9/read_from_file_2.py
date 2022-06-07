
with open('file.txt') as f:
    lines = f.readlines()
    print(type(lines))
    print(lines)
    for line in lines:
        print(line.strip('\n'))
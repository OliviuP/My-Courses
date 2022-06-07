# 3.	Write a function print_rectangle() which prints out a rectangle made of character and wall
# size defined by user.
# a.	Make the character parameter optional with default value ‘#’.
# b.	Make the wall size parameter mandatory.
# c.	For wall_size = 3 the output should be:

###
###
###

def print_rectangle():
    n = '#'
    w = int(input('Enter the wall size:'))
    for i in range(w):
        print(w*n)


print(print_rectangle())
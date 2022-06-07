# 2.	Write a function max_of_three(a, b, c) which returns the biggest of the three numbers.

def max_of_three(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > b and c > a:
        print(c)


print(max_of_three(1,2,3))
print(max_of_three(5,3,2))
print(max_of_three(3,5,4))
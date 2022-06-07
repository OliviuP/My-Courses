# Format and display (older solution)
a = 3
b = 4
my_sum=a+b
print("a=%s, b=%s, and their sum is: %s" % (a, b, my_sum)) # conteaza ordinea

# Format and display (newer solution)

print("a={}, b={}, and their sum is: {}" .format(a, b, my_sum))

print("a={val_a}, b={val_b}, and their sum is {val_my_sum}" .format(val_a=a, val_b=b, val_my_sum=my_sum)) # nu mai sunt obligat sa le dau ordine

print("a={1}, b={0}, and their sum is: {2}".format(b, a, my_sum))


# f-string interpolation - (cea mai noua)
print(f"a={a}, b={b}, and their sum is: {my_sum}")
print(f"a^b = {a ** b}")

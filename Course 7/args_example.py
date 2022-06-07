# def add_1(a, b):
#     return a + b
#
#
# print(add_1(1, 2))
#
#
# def add_2(a, b, c):
#     return a + b + c
#
#
# print(add_2(1, 2, 3))
#
#
# def add_3(a, b, c, d):
#     return a + b + c + d
#
#
# print(add_3(1, 2, 3, 4))
#
#
# def add_n(*args):
#     # *args -> ne retine intr-o lista parametrii pozitionali dati
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
# print(add_n(1,2,3,4,5,6,7,))

def print_name_and_something(name, *args):
    print(f'First name: {name}')
    print(f'Second to last name:', end='')
    for arg in args:
        print(arg, end=' ')
    print()


print_name_and_something('Ion', 'Mihai', 'Petru')
print_name_and_something('Ion')

def add_ingredients(**kwargs):
    result = 0
    for key in kwargs:
        result += kwargs[key]
    return result


print(add_ingredients(eggs=3, spam=5, cheese=2))

def print_args(*args, **kwargs):
    print('Position agruments: ')
    for elem in args:
        print(elem)
    print('Keyword arguments: ')
    for key in kwargs:
        print(kwargs[key])

print_args(3,7,9, nb_1=99, nb_2=77, nb_3=100)

# import copy
#
# my_list = [1, 2, 3, 4, 5]
# my_list_1 = my_list
# my_list_2 = copy.deepcopy(my_list_1)
# print('My_list:', my_list)
# print('My_list_1:', my_list_1)
# print('My_list_2:', my_list_2)
#
# my_list[0] = 55
# my_list_1[1] = 99
# print('My_list:', my_list)
# print('My_list_1:', my_list_1)
# print('My_list_2:', my_list_2)

# def modify_list(my_list):
#     my_list[0] = 780
#
# my_l = [7,8,9,10 ]
# print(my_l)
#
# modify_list(my_l)
# print(my_l)
import copy


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

animal_a = Animal('Rex', 22)
animal_b = animal_a # pass by reference
animal_c = copy.deepcopy(animal_a) # pass by value
animal_a.age = 100


print(animal_b.name, animal_b.age)
print(animal_c.name, animal_c.age)



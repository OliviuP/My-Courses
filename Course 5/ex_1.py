# Vrem sa calculam suma elementele unei liste.

# lst = [1, 2, 3, 4, 5, 6, 7, 10]
lst = [77, 99, 1, 0, 2, 3]
# folosind while


my_sum = 0

lst_size = len(lst)
counter = 0
while counter < lst_size:
    my_sum = my_sum + lst[counter]
    counter = counter + 1
print("Sum of elements of list is", my_sum)


# folosind for v1

my_sum = 0
for element in lst:
    my_sum += element
print(my_sum)

# folosint for v2

# my_sum = 0
# for i in range(0, len(lst)):
#     my_sum += lst[i]
# print(my_sum)

#folosind functia de sum

print(sum(lst))
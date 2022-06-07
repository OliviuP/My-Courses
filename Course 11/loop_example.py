# incrementati fiecare element dintr-o lista

my_list = [1,2,3,4,5]

# for elem in my_list: # putem vedea valoarea fiecarui element dintr-o lista, fara a o putea modifica
#     elem += 1

for i in  range(len(my_list)):
    my_list[i] += 1
print(my_list)
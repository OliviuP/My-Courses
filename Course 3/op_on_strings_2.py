my_str = "Hello, World!"
# afisam o anumita litera
print('Displaying the character at index 7: ', my_str[7])
print('Displaying the character at index 0: ', my_str[0])

# string slicing -> my_str[index_start : index_stop]
# se afiseaza caracterele pentru care index_start <= index_caracter < index_stop
print("Displaying characters from index 7 to 11:", my_str[7:13])

print("Displaying characters from index 5 till the end of the string:", my_str[5:])
print("Displaying all characters from the beginning of the string until index 5:", my_str[:6])

# facem slicing din 2 in 2

print(my_str[7:12:2])

# afisam in ordine inversa

print('Displaying the string in reverse order:', my_str[::-1])

# afisam caracterele din 3 in 3
print(my_str[::3])
print("=" * 100)
# vrem sa obtinem din stringul initial un string fara spatiul liber
# rezultatul final : Hello,World!
# solutia 1

print(my_str[:6], end="")
print(my_str[7:])

# solutia 2

print(my_str[:6] + my_str[7:])

# solutia 3

print(my_str[:6], my_str[7:], sep="")

# solutia 4 -> mai generala, dar poate elimina doar primul spatiu intalnit

searched_index = my_str.index(" ")
print(searched_index)
print(my_str[:searched_index] + my_str[searched_index + 1:])

# solutia 5
print(my_str.replace(" ", ""))
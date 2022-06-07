#o colectie de valori unice, neindexate si neordonate

# declaram un set
animals = {"dog", "cat", "elephant"}

animals.add("mouse")
print(animals)

animals.add('cat')
animals.add('dog')
print(animals)

# Afisati o lista cu elemente unice dintr-o lista

my_list = [2,2,1,7,9,0,0,3,8,1,1]
print('Initial list:', my_list)
unique_elements = list(set(my_list))
print('Unique elements:', unique_elements)

print('Unique elements:',list(set(my_list)))
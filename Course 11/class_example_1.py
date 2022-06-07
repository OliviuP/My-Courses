
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # def print_details(self):
    #     print(f"name: {self.__name}, age: {self.__age}")

    def __str__(self):
        return f"name: {self.__name}, age: {self.__age}"

    def __repr__(self): # din construcite, odata implementata, __repr__ ne permite sa printam direct o lista de obiecte
        return f"name: {self.__name}, age: {self.__age}"

    def __eq__(self, other): # equals ==
        return self.__age == other.age

    def __gt__(self, other): # greater than, >
        return self.__age > other.age

    def __lt__(self, other): #less than,  <
        return self.__age < other.age



    @property
    def age(self):
        return self.__age

def get_older_dog(dog_1, dog_2):
    #daca nu avem functiile magice implementate folosim asta:
    # if dog_1.age > dog_2.age:
    #     return dog_1
    # return dog_2

    #daca le avem folosim asta:

    if dog_1 > dog_2:
        return dog_1
    return dog_2

# daca nu implementam __str__() si scriem print(my_dog), ni se va afisa adresa de memorie a obiectului nostru
# daca implementam __str__() si scriem print(my_dog), se va afisa string-ul returnat de functie.

my_dog_1 = Animal('Rex', 2)
print(my_dog_1)

my_dog_2 = Animal('Max', 10)
print(my_dog_2)

print(my_dog_2.age)

print(f"Oldest dog is: {get_older_dog(my_dog_1, my_dog_2)}")

animal_list = [my_dog_1, my_dog_2]
#daca nu am implementat __repr__(), daca scriu print(animal_list) imi va afisa o lista de adrese de memorie
print(animal_list)
# daca nu am implementat __repr__(), cum pot vedea elementele din lista??

for animal in animal_list:
    print(animal)
#declaram un dictionar gol
car_price = {}
# cheia -> modelul masinii
# valoarea -> pretul ei

car_price['Dacia Duster'] = 10000
car_price['Dacia Logan'] = 5000
car_price['Mercedes'] = 50000

print(car_price)
print('Mercedes price is:', car_price['Mercedes'])
number_letters = {
    1: 'a',
    2: 'b',
    3: 'c',
}

print('Original number_letters dict', number_letters)
number_letters[4] = 'd'
print('After adding (4, "d") key-value pair: ' ,number_letters)
number_letters[2]= 'aa'
print('After replacing the value at key 2 with "aa:', number_letters)
del number_letters[1]
print('After deleting the (1, "a") pair:', number_letters)
number_letters.pop(4)
print('After deleting the (4, "d") pair:', number_letters)
#number_letters.get(2) si number_letters[2] ne dau aceeasi valoare
# atunci cand cheia selectata exista in dictionar, Cand nu mai exista
# functia get ne returneaza none, iar operatoruo [] ne arunca o eroare
print(number_letters.get(2))
print(number_letters[2])
# functia get() are un al doilea parametru in care specificam ce valoare sa ni se returneze atunci cand cheia cautata nu exista
print(number_letters.get(0, 'key not found :('))
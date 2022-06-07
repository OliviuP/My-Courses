# In python, putem specifica tipurile de date ale variabilelor, dar acest lucru este optional.
# Daca o variabila are specificat tipul int, iar valoarea ei este de tipul str, python va considera ca tipul de
# de date al esi este: str
# Motivul pentru care se sugereza tipul de date al variabilelor este acela de a induce ce tipuri de date si-a dorit
# sa fie utilizate cel care a scris codul.
a = 5
print(type(a))

b: int = 'abcd' # desi am sugerat ca tipul de date este int, in realitate python isi ia tipul de date din valoarea
# data variabilei, ingnorand practic sugestia noastra
print(type(b))

def add(a: int,b: int) -> int:
    return a + b

print(add(2, 3))
print(add('2', '3'))
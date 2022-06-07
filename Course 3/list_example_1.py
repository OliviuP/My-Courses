# declaram o lista goala

alphabet = []
print('List is:', alphabet)
print('Lenght of the list:', len(alphabet))
alphabet.append('a')
alphabet.append('b')
alphabet.append('c')


print('List is', alphabet)
print('Lenght of the list', len(alphabet))

print('first element of the list is:', alphabet[0])
# calculam noi indexul ultimului element
print('Last element of the list is:', alphabet[len(alphabet)-1])

# aici afisam direct ultimul element
print('Last element of the list is:', alphabet[-1])

# extend() ne permite sa extindem lista noastra cu o alta lista

alphabet.extend(["f", "d", "g", "e"])
print('List (confused) is:', alphabet)

# functia de sortare din python poate fi folosita pentru string-uri, numbere
# si altele. Ea vine in 2 variante
# - list.sort() -> sorteaza lista initiala
# - sorted(list) -> returneaza o lista cu elementele sortate, pastrand lista initiala intacta

print('List (sorted) is:', sorted(alphabet)) # lista initiala nu s-a modificat
alphabet.sort() # lista initiala s-a modificat, elementele fiind acum sortate
print('List (sorted) is:', alphabet)

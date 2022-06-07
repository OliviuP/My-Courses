# a) Scrieti o functie numita do_operation() cu 3 parametri:
# - primul numar -> un nr intreg
# - al doilea numar -> un nr intreg
# - al treilea numar care specifica operatia selectata:
# 1- adunare
# 2 - scadere
# 3-  inmultire,
# 4 - impartire
# Orice alt numar dat celui de-al treilea parametru, va rezulta in afisarea unui mesaj de eroare.
# Rezultatul se va afisa din interiorul functiei
# b) Modificati functia de mai sus astfel:
# - parametrul c va deveni parametru optional cu vloarea implicita  = 1
# - valoare aoperatiei va fi returnata si apoi afisata
# - cititi primii 2 parametrii  de la tastatura
# - modificati primii 2 parametrii a. i. ei sa devina optionali (5 si 2 )

def do_operation(a=5, b=2, c=1):
    if c == 1:
        return a + b
    elif c == 2:
        return a - b
    elif c == 3:
        return a * b
    elif c == 4:
        return a / b
    else:
        print(f"Valorea {c} introdusa nu este valida! Alegeti una din variantele 1,2,3 sau 4.")

#return -> returneaza(scoate) valoarea operatiei din functie, valoare ce va fi apoi afisata in afara ei
x=int(input('x = '))
y=int(input('y = '))
# putem da parametrii dupa pozitie
result_1 = do_operation(x, y, 1)
print(result_1)
# sau dupa nume
result_2 = do_operation(a=x, b=y, c=4)
print(f'{result_2: .3f}')
#dand parametrii dupa nume, ii putem pune in ce ordine dorim
print(do_operation(c=3, a=x, b=y))


print(do_operation(x, y, 7)) # se afiseaza None, pentru ca functia pe ramura de else nu returneaza nimic

# pentru ca C este parametru optional, nu mai sunt obligat sa il dau la apelul functiei
print(do_operation(x, y))

print('='*50)

print(do_operation()) #pot apela asa pentru ca cei 3 parametrii sunt optionali
print(do_operation(c=4)) # a si b vor avea valorile implicite 5 si 2




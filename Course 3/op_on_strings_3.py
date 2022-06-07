# strip() elimina spatiile libere de la inceputul si finalulk stringului

my_str = "   Hello World!     "
print(f'Raw string: {my_str} ')

my_str_stripped = my_str.strip()

print(f'Processed string: {my_str_stripped}')

# transformam literele mici in litere mari

print(my_str_stripped.upper())

# transformam din litere mari in litere mici

print(my_str_stripped.lower())

lower_characters_str = my_str_stripped.lower()
# transform primul caracter din litera mica in litera mare
print(lower_characters_str.capitalize())

print('=' * 50)
my_str_1 = "ce Mult Imi Place Programarea"
print(my_str_1.capitalize())

#functia de replace are 3 parametri:
# - primul, este stringul pe care il vrem sa fie inlocuit
# - al doliea, este stringul cu care vrem sa se inlocuieasca cel initial
# - al treilea, ne spune de cate ori vrem sa inlocuim stringul pe care il gaseste

print(my_str_1.replace(my_str_1[0], my_str_1[0].upper(), 1))

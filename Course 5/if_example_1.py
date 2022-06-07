
x = int(input("Enter a number: "))
if x < 10:
    # linia aceasta de cod se va rula numai daca x < 10
    print(f'{x} is less than 10')
elif x == 10:
    print(f'{x} is equal to 10')
else:
    print(f'{x} is greater than 10')
print('End of program')
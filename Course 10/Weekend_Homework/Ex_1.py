# 1.	Write an application that:
# a.	Asks user for an input in a loop and prints it out.
# b.	If the input is equal to “exit”, program terminates printing out provided input and “Done.”.
# c.	If the input is equal to “exit-no-print”, program terminates without printing out anything.
# d.	If the input is equal to “no-print”, program moves to next loop iteration without printing anything.

while True:
    n = str(input("Write here: "))
    if n == 'exit':
            print(n)
            print("Done")
            break
    elif n == 'exit-no-print':
            break
    elif n == 'no-print':
            continue




password = input('Enter the password: ')

a = (len(password) - 2) * '*'
b = password + '**********'

if len(password) < 6:
    print(b[:6])
elif len(password) >= 6:
    print(password[0] + a + password[-1])

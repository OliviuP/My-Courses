class User:
    # declar constructorul clasei
    # functia constructor se apeleaza atunci cand creez un obiect nou
    def __init__(self, username='user123', password='ak47'):
        self.username = username
        self.password = password

    def print_details(self):
        print(f'username: {self.username}, password: {self.password}')

class Product:
    def __init__(self):
        pass



user_dorin = User('dorin_64', 'ciresica23')
print(type(user_dorin))
print('Details of user_dorin:')
user_dorin.print_details()


user_default = User()
print('Details of user_default:')
user_default.print_details()

another_user = User('another_one')
another_user.print_details()

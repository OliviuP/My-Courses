
class User:
    #declar constructorul clasei
    #functia constructor se apeleaza atunci cand creez un obiect nou
    def __init__(self):
        self.username = 'user123'
        self.password = 'ak47'

    def print_details(self):
        print(f'username: {self.username}, password: {self.password}')


user_dorin = User()
print(type(user_dorin))
user_dorin.print_details()
user_dorin.username = 'dorin_64'
user_dorin.password = 'ciresica23'
user_dorin.print_details()

user_default = User()
user_default.print_details()
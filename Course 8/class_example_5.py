class User:
    def __init__(self, username, password, has_access=False):
        self.username = username  # este membru public
        self.__password = password  # password este membru privat,
        self._has_access = has_access # este membru protejat
    def print_details(self):
        print('Username :', self.username, 'password', self.__password, 'has accesss:', self._has_access)

    @property
    def password(self): #-> echivalent cu getterul
        return self.__password

    @password.setter
    def password(self, new_password):
        if self._has_access:
            self.__password = new_password
        else:
            print("Sorry you don't have access to change your password")




admin = User('admn', 'asdf', True)
admin.print_details()
admin.password = '1234'
admin.print_details()
print('password:', admin.password)
print('='*30)
other_user = User('usr', '7890')
other_user.print_details()
other_user.password = '1234'
other_user.print_details()

print('password:', other_user.password)


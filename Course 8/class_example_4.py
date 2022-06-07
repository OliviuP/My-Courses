class User:
    def __init__(self, username, password, has_access=False):
        self.username = username  # este membru public
        self.__password = password  # password este membru privat,
        self._has_access = has_access # este membru protejat
    def print_details(self):
        print('Username :', self.username, 'password', self.__password, 'has access:', self._has_access)

    def set_password(self, new_password):
        if self._has_access:
            self.__password = new_password
        else:
            print("Sorry you don't have access to change your password")

    def get_password(self):
            return self.__password




admin = User('admn', 'asdf', True)
admin.print_details()
admin.set_password('1234')
admin.print_details()
print('password:', admin.get_password())
print('='*30)
other_user = User('usr', '7890')
other_user= User('admn', 'asdf')
other_user.print_details()
other_user.set_password('1234')
other_user.print_details()





# print('Username :', admin.username, 'password', admin.__password)
# pot incerca sa modific __password, dar nu se modifica membrul clasei pe care l-as fi vrut modificat
# admin.__password = 'ak47'
# admin.print_details()
#
# print(admin.__password)

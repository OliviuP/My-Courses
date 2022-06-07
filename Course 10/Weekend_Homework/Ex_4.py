# 4.	Create User class with name and password fields.
# a)	The name field should be accessible and the password field should be private and accessed through a property.
# b)	The initialization method (the constructor) should accept only the name field.
# c)	The password’s setter should check if the password is at least 6 characters long,
# if it is less then it should extend the provided value to 6 characters by adding appropriate
# number of “#” characters (‘ab’ -> ‘ab####’). If the password is 6 or more characters long then it should not modify it.
# d)	The getter should return the password in an encrypted format, that is replacing all letters
# except first and last with the “*” character (‘password’ -> ‘p******d’).

class User:
    def __init__(self, name , password, has_access = False):
        self.name = name
        self.__password = password
        self._has_access = has_access

    def print_details(self):
        print('Username: ', self.name, 'Password: ', self.__password, 'property', self._property)

    @property
    def password(self):
        a = (len(self.__password) - 2) * '*'
           return self.__password[0] + a + self.__password[-1])

    @password.setter
    def password(self, new_password):
        b = new_password + "#######"
        if self._has_access:
            self.__password = new_password
        else:
            print("Sorry, you don't have the access to change your password")
        if len(new_password) < 6:
            print(b[:6])
        else:
            print(new_password)

admin = User("Admin", "fadsfafa", True)
admin.password = "jaajjij"
print(admin.password)




class User:
    def __init__(self, name):
        self.name = name
        self.__password = None

    @property
    def password(self):
        a = (len(self.__password) - 2) * '*'
        return self.__password[0] + a + self.__password[-1]

    @password.setter
    def password(self, new_password):
        # b = new_password + "######"
        # if len(new_password) < 6:
        #     self.__password = b[:6]
        # else:
        #     self.__password = new_password
        #
        # # sau

        if len(new_password) < 6:
            self.__password = new_password + ("#" * (6 - len(new_password)))

user_1 = User('admin')
user_1.password = 'abcdefghij'
print(f'username: {user_1.name}, password: {user_1.password}')

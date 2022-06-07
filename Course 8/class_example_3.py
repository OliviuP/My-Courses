
class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password

#Exista 3 specificatori de acces:
# - public -> campurile si metodele pot fi accesate de oriunde din afara clasei
# - protected -> o practica buna ar fi ca campurile si metodele sa poate fi accesate direct doar din interiorul clasei
# - private -> campurile si metodele nu pot fi accesate direct din interiorul clasei, ci doar din interiorul ei
# -

# Desi python-ul nu ne arunca o eroare, idicat este sa nu accesam direct campurile si metodele protected dintr-o clasa,
# ci sa implementam setteri, respectivi getteri.
# In general, protected inseamna public pentru clasele copil

admin = User('admn', 'adsf' )

print('Username password:', admin.username, admin._password)
admin.password = '1996'
print('Username password:', admin.username, admin._password)

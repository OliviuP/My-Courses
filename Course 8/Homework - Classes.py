# Create Vehicle class with fields: name, type, color and price and methods: description() that
# returns a string describing the vehicle.
# a)	The Vehicle class initialization method should require name and price parameters and have default values for type and color.
# b)	Create vehicles list.
# c)	Write a loop that asks user 3 times for input regarding vehicle creation. With each loop
# iteration user should provide name and price and should be asked if he wants to provide type
# and color. If the user responds yes, he should be asked for the type and color. Once the input
# is collected, create new vehicle based on the input and add it to the vehicles list.
# In a loop, print details of each car in the cars list.


class Vehicle:
    def __init__(self, name, price, type='Sedan', color='grey'):
        self.name = name
        self.type = type
        self.color = color
        self.price = price

    def description(self):
        return f'name: {self.name} , type: {self.type}, color: {self.color}, price: {self.price} '

def show_vehicle_list(vehicle_lst):
    print("Vehicle list:")
    for vehicle in vehicle_lst:
        print(vehicle.description())


vehicle_list= []

for i in range(3):
    name =  input('Name= ')
    price = input('Price= ')
    choise = input('Do you want to enter the type and color (Yes/No, Y/N):')
    if choise == 'Yes' or choise == 'Y':
        type = input('Type= ')
        color = input('Color= ')
        my_vehicle = Vehicle(name, price, type, color)
    else:
        my_vehicle = Vehicle(name, price)
    vehicle_list.append(my_vehicle)

show_vehicle_list(vehicle_list)



# vehicle_1 = Vehicle('Dacia', 2000, 'Logan', 'blue')
# vehicle_2 = Vehicle('Honda', 6000, 'Civic 8')
# vehicle_3 = Vehicle('BMW', 10_000, 'M3', 'black')
#
# vehicle_list = [vehicle_1, vehicle_2, vehicle_3]
#
# for vehicle in vehicle_list:
#     print(vehicle.description())




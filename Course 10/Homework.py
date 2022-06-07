# elements_list = [['Dacia', 2000, 'Logan', 'blue'], ['Honda', 6000, 'Civic 8', 'brown'], ['BMW', 10_000, 'M3', 'black']]
# a. Scrieti elementele din lista de mai sus, cate un element pe rand in fisierul 'vehicles.txt'
# b. Cititi fisierul si pentru fiecare rand, creati un obiect de tip Vehicle si adaugati-l intro lista de obiecte.
# c. Afisati lista de obiecte.
#
# indiciu: folositi functia split(', ') ca sa separati elementele dupa de cititi cate un rand din fisier.

# element_1 = ['Dacia', 2000, 'Logan', 'Blue']

elements_list = [['Dacia', 2000, 'Logan', 'blue'], ['Honda', 6000, 'Civic 8', 'brown'], ['BMW', 10_000, 'M3', 'black']]


# =================================
#
# with open('Vehicle.txt', 'w') as f:
#     for element in elements_list:
#         f.write(f"{element} \n")
#
# vehicles_1 = ["Mercedes", 11_000, "C Klassse", "Red"]
# vehicles_2 = ["Alfa Rome", 6000, "Julietta", "grey"]
# vehicles_3 = ["Dacia", 5000, "Duster", "Grey"]
#
# vehicles_list =(vehicles_1, vehicles_2, vehicles_3)
#
# with open('Vehicle.txt', 'a') as f:
#     for cars in vehicles_list:
#         f.write(f'{cars} \n')
# ==================================================
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


def write_list_to_file():
    with open('vehicles.txt', 'w') as f:
        for elem in elements_list:
            for sub_elem in elem:
                value_to_write = str(sub_elem) if type(sub_elem) == int else sub_elem
                f.write(value_to_write + ', ')
            f.write('\n')


def read_list_from_file():
    vehicle_list = []
    with open('vehicles.txt') as f:
        rows_list = f.readlines()
        for row in rows_list:
            row = row.strip().split(',')
            name = row[0]
            price = int(row[1])
            type = row[2].strip()
            color = row[3].strip()
            my_vehicle = Vehicle(name, price, type, color)
            vehicle_list.append(my_vehicle)

    return vehicle_list


vehicle_list = read_list_from_file()
write_list_to_file()

show_vehicle_list(vehicle_list)


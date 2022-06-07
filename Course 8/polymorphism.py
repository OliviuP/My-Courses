
#DEFINITIE:  intr-o ierarhie de mosteniri , clase diferite, raspund in mod diferit apelului aceleasi functii

class Animal:
    def __init__(self):
        pass

    def make_noise(self):
        print('Abstract noise')


class Mammal(Animal):
    def __init__(self):
        pass

    def make_noise(self):
        print('General mammal noise')


class Dog(Mammal):
    def __init__(self):
        pass

    def make_noise(self):
        print('Ham Ham')


class Cat(Mammal):
    def __init__(self):
        pass

    def make_noise(self):
        print('Miau miau')
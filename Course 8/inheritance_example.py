
class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

class Programmer(Human):
    def __init__(self, name, height, weight, languages):
        # super().__init__(name, height, weight)
        Human.__init__(self, name, height, weight)
        self.languages = languages

bob = Programmer("Bob", 180, 100, ["Python", "Java"])
print(bob.name)
print(bob.weight)
print(bob.languages)
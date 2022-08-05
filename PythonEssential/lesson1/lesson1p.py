class Person:
    def __init__(self, name, age):  # конструктор
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, 'is', self.age)


# john = Person()
# john.name = 'John'
# john.age = 22

# luci = Person()
# luci.name = 'Luci'
# luci.age = 21

# print(john.name, 'is', john.age)
# print(luci.name, 'is', luci.age)
# Person.print_info(john)
# Person.print_info(luci)
john = Person('John', 22)
luci = Person('Luci', 21)


john.print_info()
luci.print_info()

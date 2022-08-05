class MyObject:
    def __init__(self):
        self.__private_attribute = 42

    def get_attribute(self):
        return self.__private_attribute

    def set_attribute(self, value):
        self.__private_attribute = value

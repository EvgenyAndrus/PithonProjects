from lesson2_check_instance import check_instance, check_subclass


class Animal:
    can_run = bool
    can_fly = bool

    def __init__(self):
        self.can_run = False
        self.can_fly = False

    def print_abilities(self):
        print(type(self).__name__ + ':')
        print('Can run:', self.can_run)
        print('Can fly:', self.can_fly)
        print()


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Pegasus(Horse, Bird):
    pass


def main():
    horse = Horse()
    horse.print_abilities()

    bird = Bird()
    bird.print_abilities()

    pegasus = Pegasus()
    pegasus.print_abilities()

    print(check_instance(bird, Animal))  # obj является экземпляром класс cls
    print('isinstance(pegasus, Bird)', isinstance(pegasus, Bird))
    print(check_subclass(Pegasus, Animal))  # Pegasus является подклассом класса Horse
    print(check_subclass(Bird, Animal))
    print('issubclass(Bird, Animal)', issubclass(Bird, Animal))
    print(check_instance(True, int))
    print(check_instance(8, str))


if __name__ == '__main__':
    main()

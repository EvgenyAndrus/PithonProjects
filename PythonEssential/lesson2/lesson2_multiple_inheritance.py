class Horse:
    def run(self):
        print('I am run!')


class Bird:
    def fly(self):
        print('I am flying!')


class Pegasus(Horse, Bird):
    pass


def main():
    pegasus = Pegasus()
    pegasus.run()
    pegasus.fly()


if __name__ == '__main__':
    main()

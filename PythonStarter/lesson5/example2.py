import example1


def print_numbers(limit):
    for i in range(limit):
        print(i)


def main():
    example1.hello()
    print_numbers(3)
    print()
    print_numbers(5)


if __name__ == '__main__':  # проверяет что
    main()                  # данный модуль был запущен
                            # как основная программа

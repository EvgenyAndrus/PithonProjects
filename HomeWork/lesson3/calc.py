"""Напишите программу-калькулятор, которая поддерживает следующие операции:
сложение, вычитание, умножение, деление и возведение в степень.
Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных,
делении на ноль и возведении нуля в отрицательную степень.  """
import sys


def addition(f_number, s_number):
    return f_number + s_number


def subtraction(f_number, s_number):
    return f_number - s_number


def multiplication(f_number, s_number):
    return f_number * s_number


def division(f_number, s_number):
    return f_number / s_number


def exponentiation(f_number, s_number):
    return pow(f_number, s_number)


def operations(f_number, s_number, operation):
    match operation:
        case 0:
            print('quit')
            sys.exit()
        case 1:
            print('addition')
            print('first number + Second number =', addition(f_number, s_number))
        case 2:
            print('subtraction')
            print('first number - Second number =', subtraction(f_number, s_number))
        case 3:
            print('multiplication')
            print('first number * Second number =', multiplication(f_number, s_number))
        case 4:
            print('division')
            try:
                print('first number * Second number =', division(f_number, s_number))
            except ZeroDivisionError:
                print('error Zero Division')
                raise

        case 5:
            try:
                print('exponentiation')
                print('first number ^ Second number =', exponentiation(f_number, s_number))
            except ZeroDivisionError:
                print('0 cannot be raised to a negative power')
                raise
        case _:
            raise ValueError


def main():
    while True:
        print('Calculator')
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            print('menu')
            print('1: addition\n'
                  '2: subtraction\n'
                  '3: multiplication\n'
                  '4: division\n'
                  '5: exponentiation\n'
                  '0: quit\n')
            operations(first_number, second_number, int(input('choose operation: ')))
            break
        except (ValueError, ZeroDivisionError):
            print('incorrect value')


if __name__ == '__main__':
    main()

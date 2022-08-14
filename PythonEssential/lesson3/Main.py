from lesson3_4 import print_result


def main():
    while True:
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            # print('Result: ', first_number / second_number)
            result = first_number / second_number
        except (ValueError, ZeroDivisionError) as error:
            print('Error: ', error)
            print('please try again')
        else:  # перенесено в else чтобы ловить ошибку не связанную с пользователем
            print_result(result)  # 0 / 5  здесь ошибка
            break
        finally:  # выполняется всегда
            print('Finally block')


if __name__ == '__main__':
    main()

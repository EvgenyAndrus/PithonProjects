def main():
    try:
        raise ValueError('value incorrect')
    except ValueError as error:
        print('Exception: ', error)
        raise  # выбросить исключение дальше


try:
    main()

except ValueError:
    print('Value error detected')

number = int(input('Enter an integer: '))
if number:
    print('The number is nit zero')
else:
    print('The number is zero')

string = input('Enter a string: ')
if string:  # <- эквивалентно if string != '':
    print('The string is "{}"'.format(string))


number = float(input('Enter a num: '))
if 0 < number <= 7:
    print('Value is in range')
elif number < 0:
    print('value is negative')
elif number > 7:
    print('Value greater 7')
else:
    print('value = 0')

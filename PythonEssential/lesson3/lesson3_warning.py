import warnings

name = input('enter your first and last name: ')

if name.count(' ') != 1:
    warnings.warn('name format may be incorrect')

print('hello,', name, '!', sep='')

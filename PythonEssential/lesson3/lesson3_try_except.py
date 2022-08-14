# не явное вложение try - except
def do_stuff2():
    try:
        do_stuff()
    except AttributeError:
        print('AttributeError')


def do_stuff():
    try:
        raise ValueError
    except ZeroDivisionError:
        print('ZeroDivisionError')


try:
    do_stuff2()
except ValueError:
    print('ValueError')

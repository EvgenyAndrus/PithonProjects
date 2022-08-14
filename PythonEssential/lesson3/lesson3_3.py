a = 5
b = 0

try:
    result = a / b
except ZeroDivisionError as error:  # ZeroDivisionError причина ошибки ValueError
    raise ValueError('variable b is incorrect')

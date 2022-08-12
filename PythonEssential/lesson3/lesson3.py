print('Calculator')

a, b = 5, 0
try:
    print(a/b)
except ZeroDivisionError:
    print('error division by zero')
print('stopping calculator')

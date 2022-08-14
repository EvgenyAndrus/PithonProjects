print('Calculator')

try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a/b)
# except ZeroDivisionError:
#     print('error division by zero')
# except ValueError:
#     print('error ValueError')
except (ZeroDivisionError, ValueError) as error:
    print(error)
print('stopping calculator')
 
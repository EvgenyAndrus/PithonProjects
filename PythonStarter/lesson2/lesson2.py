from math import pi, sin, hypot, sqrt

# числа типа int
myInt = 234324
print(myInt)
print(type(myInt))
myBinary = 0b001010101
print(myBinary)
print(type(myBinary))
myOctal = 0o7352
print(myOctal)
print(type(myOctal))
myHexadecimal = 0xabcdf
print(myHexadecimal)
print(type(myHexadecimal))
number = 23462456
print(number)
print('---------------------------------')
# строка
myStr = 'hello'
print(type(myStr))
print(myStr)
myStr = '786234862'
print('строка', myStr)
number = int(myStr)  # преобразование строки в int
print('число типа int', number)
print('---------------------------------')
# bool
x = True
print(x)
print(type(x))
print(int(x))
y = False
print(y)
print(type(y))
print(int(y))
print(x + True)
print('---------------------------------')
# float числа c плавающей точкой
myFloat = 0.5
print(myFloat)
print(type(myFloat))
myFloat = -1.
print(myFloat)
print(type(myFloat))
myFloat = 3.2e5
print(myFloat)
print(type(myFloat))
myFloat = 3.2e-3
print(myFloat)
print(type(myFloat))
print(myInt, "int to float", float(myInt))
print(myStr, 'str to float', float(myStr))
# комплексные числа
print('---------------------------------')
myComplex = 2 + 3j
print(myComplex)
print(type(myComplex))
myComplex = complex(2, 3)
print(myComplex)
print(type(myComplex))
myComplex = complex(5, -7)
print(myComplex)
print(type(myComplex))
myStr = '8-3j'
myComplex = complex(myStr)
print(myComplex)
print(type(myComplex))
print('---------------------------------')
# динамическая типизация
var = 'I am a string'
print(var)
print(type(var))
var = 654654
print(var)
print(type(var))
print('---------------------------------')
# сильная типизация
a = 11
b = 8
print(a + b)
b = "8"
# print(a + b)  # ошибка
# операции с числами
print('---------------------------------')
x = -10
y = 3
print('x =', x, 'y =', y)
print('сложение', x + y)
print('вычитание', x - y)
print('умножение', x * y)
print('деление', x / y)
print('целочисленное деление', x // y)
print('остаток от деления', x % y)
print('модуль числа', abs(x / y))
print('степень', pow(x, y))  # или x ** y
print('корень 16', sqrt(16))
print('округление', round(x / y, 3))
print('---------------------------------')
print('число Пи', pi)
print(sin(pi / 4))
print('гипотенуза по 2м катетам с размерами 3 и 4 =', hypot(3, 4))
print('------------------------------------------------------------------')
# логические операции
print(True and True)
print(True or False)
print(True and False)
print(not True, "\n")
print(2 < 3)
print(2 == 3)
print(2 != 3)
print(2 > 3, '\n')
# строки
string1 = 'string'
string2 = "string"
print(string1, string2)
string = 'first line ' \
         'second line ' \
         "third line"
print(string)
string = 'first line\n' \
         'second line\n' \
         "third line"
print(string)
print('------------------------------------------------------------------')
# вывод на экран
print(2, 3, 5)
print(2, 3, 5, sep=',')
print('he', 'llo', sep='')
print(1, end='\n\n')
print(2)
# ввод
print('------------------------------------------------------------------')
string = input('enter a string: ')
print('you have entered "{}"'.format(string))
print('Press Enter to continue...')
input()

n = int(input('first num: '))
m = int(input('second num: '))
print('{} + {} = {}'.format(n, m, n + m))

class A:
    def method(self):
        print('A method')


class B(A):
    pass


class C(A):
    def method(self):
        print('C method')


class D(B, C):
    pass


# mro (MethodResolutionOrder)
# Порядок,в котором интерпретатор просматривает базовые классы,
# определяется линеаризацией данного класса
# Она хранится в атрибуте класса __mro__.
# MRO строится при помощи алгоритма C3-линеаризации.

#  o = D()
#  o.method()
#  print(D.mro())

for cls in [A, B, C, D]:
    print(cls.__name__ + ':', cls.mro())

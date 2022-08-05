class Complex:
    real = float
    imaginary = float

    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):  # сообщение для разработчиков
        return 'Complex({!r}, {!r})'.format(self.real, self.imaginary)

    def __str__(self):  # сообщение для ползователей
        return '{}{:+d}i'.format(self.real, self.imaginary)

    def __add__(self, other):  # сложение
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __neg__(self):  # унарный минус
        return Complex(-self.real, -self.imaginary)

    def __sub__(self, other):  # вычитание
        return self + (-other)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary




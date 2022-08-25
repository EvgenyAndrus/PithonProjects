"""Задание 1
Напишите итератор, который возвращает элементы заданного списка
в обратном порядке (аналог reversed).
"""


class MyReversed:
    def __init__(self, data):
        self.lst = data
        self.start = len(self.lst)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.start -= 1
            if self.start == -1:
                raise StopIteration
            return self.lst[self.start]


lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in MyReversed(lst):
    print(i)

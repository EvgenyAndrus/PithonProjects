"""Задание 2
Перепишите решение первого задания с помощью генератора.
"""


class MyReversed:
    def __init__(self, lst):
        self.len_list = len(lst)
        self.lst = lst
        self.start_list = self.len_list - 1

    def __iter__(self):
        while self.start_list >= 0:
            yield self.lst[self.start_list]
            self.start_list -= 1


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
    for i in MyReversed(lst):
        print(i)

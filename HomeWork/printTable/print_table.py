"""Напишите функцию printTable(), которая принимает список списков строк
и отображает его в виде аккуратной таблицы с выравниванием текста по правому краю
в каждом столбце.
Вывод функции printTable() будет примерно таким
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
"""

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(data):
    #    col_widths = [0] * len(table_data)
    length = 0
    for i in data:
        for j in i:
            if length < len(j):
                length = len(j)
    x = len(data)
    y = len(data[0])
    for j in range(y):
        for i in range(x):
            print(data[i][j].rjust(length), end='')
        print()


if __name__ == '__main__':
    print_table(table_data)

my_list = [5, 7, 9, 1, 1, 2]

sub_list = my_list[:3]  # начальный индекс можно не указывать
print(sub_list)

print(my_list[2:-2])
print(my_list[4:5])
print('-------------------------')

sub_list = my_list[:-1:2]
print(sub_list)
print(my_list[2:-2:2])

print(my_list[-1:0:-1])  # в обратном порядке без нулевого элемента
print(my_list[::-1])
print('-------------------------')

print(my_list[2:])
print(my_list[2::2])
print(my_list[:-2])
print(my_list[::-2])

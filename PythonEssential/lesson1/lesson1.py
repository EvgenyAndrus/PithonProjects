class MyObject:
    int_field = 8  # атрибут класса
    str_field = 'a string'  # атрибут класса


print(MyObject.int_field)
print(MyObject.str_field)

obj1 = MyObject()
obj2 = MyObject()

print(obj1.int_field)
print(obj2.str_field)

MyObject.int_field = 10
print(MyObject.int_field)
print(obj1.int_field)

obj1.str_field = 'another string'  # атрибут данных класса obj1

print(MyObject.str_field)
print(obj1.str_field)
print(obj2.str_field)



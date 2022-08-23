def generator_function():
    for x in range(5):
        for y in range(3):
            if (x + y) % 2 == 0:
                yield x * y


# тоже что и generator_function() только одним вырадением
generator = (x * y for x in range(5) for y in range(3) if (x + y) % 2 == 0)
for value in generator:
    print(value)
print('--------------------------------------')
print(sum(x ** 2 for x in range(10)))


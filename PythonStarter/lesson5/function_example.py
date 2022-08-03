def print_numbers(limit):
    print('id = ', id(limit))
    for i in range(limit):
        print(i)
    limit += 1
    print('limit = ', limit)
    print('id = ', id(limit))


n = int(input('n = '))
print_numbers(n)
print('n = ', n)
print('n id = ', id(n))

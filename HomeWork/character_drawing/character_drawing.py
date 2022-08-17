grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['.', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = len(grid)
y = len(grid[0])

print('\n--== before ==--\n')
for i in range(x):
    for j in range(y):
        print(grid[i][j], end='')
    print()
print('\n--== after ==--\n')

for j in range(y):
    for i in range(x):
        print(grid[i][j], end='')
    print()

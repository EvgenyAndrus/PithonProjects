def nonrecursive_factorial(n):
    result = 1
    for multiplier in range(2, n + 1):
        result *= multiplier
    return result


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(nonrecursive_factorial(1000))
#  print(recursive_factorial(1000))  # RecursionError: maximum recursion depth exceeded in comparison

def outer_function():
    def inner_function():
        print('Inner function')

    print('Outer function')
    inner_function()


outer_function()

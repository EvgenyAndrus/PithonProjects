def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():
    #    yield from range(10)
    yield '[generator]    start'
    yield from subgenerator()
    yield '[generator]      end'


for value in generator():
    print(value)

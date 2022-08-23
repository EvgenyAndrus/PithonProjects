import math


class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second

        if step != 0:
            self.step = step
        else:
            raise ValueError('Step cannot be zero')

        self.length = math.ceil((self.end - self.start) / self.step)

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.start
        for _ in range(len(self)):
            yield current
            current += self.step

    def __repr__(self):
        return 'MyRange({}, {}, {})'.format(self.start, self.end, self.step)


if __name__ == '__main__':
    for i in MyRange(5):
        print(i)
    print('----------------------------')
    for i in MyRange(10, 4, -2):
        print(i)

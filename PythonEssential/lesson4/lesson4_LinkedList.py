class List:
    class _Node:
        __slots__ = ('value',
                     'next')  # кортеж для хранения имен атрибутов. для них заранее будет выделена память и нельзя будет добовлять другие атрибуты

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    class _NodeIterator:
        def __init__(self, first):
            self._next_node = first

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        self._head = None  # указывает на первый элемент в списке
        self._tail = None  # указывает на последний элемент в списке для быстрого и эфективного добавления элементов в конец списка
        self._length = 0  # длина списка

        if iterable is not None:
            self.extend(iterable)

    def __len__(self):
        return self._length

    def append(self, value):
        node = List._Node(value)

        if len(self) == 0:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node

        self._length += 1

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return List._NodeIterator(self._head)


if __name__ == '__main__':
    numbers = List(range(100000))
    for x in numbers:
        if x % 10000 == 0:
            print(x)

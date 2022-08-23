"""
реализовывалось до версии 3.4
кооперативная многозадачность
реализация сопрограмм при помощи конструкции yield from"""
import random
import time


def sleep(seconds):
    start = time.time()
    while time.time() - start < seconds:
        yield

def produce():
#def produce(consumer):
#    while True:
    yield from sleep(0.5)
    data = random.randint(1, 100)
#   consumer.send(data)
    return data


def consume():
    sum_ = 0
    count = 0

    while True:
#        data = yield
        data = yield from produce()
        print('got data: ', data)

        sum_ += data
        count += 1

        print('Sum: ', sum_)
        print('Average: ', sum_ / count)
        print('-----------------')


def another_task():
    while True:
        print('-----------------')
        print('Hello in other task!')
        print('-----------------')
        yield from sleep(1)


if __name__ == '__main__':
    consumer = consume()
    task = another_task()

    while True:
        next(consumer)
        next(task)


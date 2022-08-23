'''декоратор @asyncio.coroutine устарел, начиная с Python 3.8  '''
import random
import asyncio


@asyncio.coroutine
def produce():
    yield from asyncio.sleep(0.5)
    data = random.randint(1, 100)
    return data


@asyncio.coroutine
def consume():
    sum_ = 0
    count = 0

    while True:
        data = yield from produce()
        print('got data: ', data)

        sum_ += data
        count += 1

        print('Sum: ', sum_)
        print('Average: ', sum_ / count)
        print('-----------------')


@asyncio.coroutine
def another_task():
    while True:
        print('-----------------')
        print('Hello in other task!')
        print('-----------------')
        yield from asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [consume(), another_task()]
    loop.run_until_complete(asyncio.wait(tasks))

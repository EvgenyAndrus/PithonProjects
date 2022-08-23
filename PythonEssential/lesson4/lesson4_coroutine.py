'''async/await'''
import random
import asyncio


async def produce():
    await asyncio.sleep(0.5)
    data = random.randint(1, 100)
    return data


async def consume():
    sum_ = 0
    count = 0

    while True:
        data = await produce()
        print('got data: ', data)

        sum_ += data
        count += 1

        print('Sum: ', sum_)
        print('Average: ', sum_ / count)
        print('-----------------')


async def another_task():
    while True:
        print('-----------------')
        print('Hello in other task!')
        print('-----------------')
        await asyncio.sleep(1)


if __name__ == '__main__':
    tasks = [consume(), another_task()]
    asyncio.run(asyncio.wait(tasks))

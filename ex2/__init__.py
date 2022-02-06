import time
from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        def benchmark(*args, **kwargs):
            total_time = 0
            for i in range(num):
                start = time.time()
                func(*args, **kwargs)
                duration = time.time() - start
                print(f'run # {i} - {duration}')
                total_time += duration
            print (f'average - {total_time/num}')
        return benchmark
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)

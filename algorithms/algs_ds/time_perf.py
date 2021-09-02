from time import perf_counter
import functools


def time_prefomance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Execution time is {end - start}')
        print(result)
        return result
    return wrapper

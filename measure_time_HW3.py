
import timeit

def measure_time(sort_func, data):
    def wrapper():
        sort_func(data.copy())
    return timeit.timeit(wrapper, number=1)

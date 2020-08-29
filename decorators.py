# Timing decorator

import functools
from time import perf_counter


def timer(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        result = f(*args, **kwargs)
        duration = perf_counter() - time_start
        print(f"func: {f.__name__}, args:{args}, kwargs: {kwargs} took {duration:.2f} sec")
        return result

    return wrapper

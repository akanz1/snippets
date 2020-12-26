# Timing decorator

import functools
from time import perf_counter


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        result = func(*args, **kwargs)
        duration = perf_counter() - time_start
        print(
            f"func: {func.__name__}, args:{args}, kwargs: {kwargs} took {duration:.4f} sec"
        )
        return result

    return wrapper

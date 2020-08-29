# Runtime decorator

import functools
from time import time


def runtime(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        time_start = time()
        result = f(*args, **kwargs)
        duration = time() - time_start
        print(f"func: {f.__name__}, args:{args}, kwargs: {kwargs} took {duration:.2f} sec")
        return result

    return wrapper

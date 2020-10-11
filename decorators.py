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
            f"func: {func.__name__}, args:{args}, kwargs: {kwargs} took {duration:.2f} sec"
        )
        return result

    return wrapper


# Logging Decorator
import functools
import logging
import os
import sys
from datetime import datetime


def logger(to: str = "stdout"):
    def _logger(func):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logs_dir = "logs"
        log_file_name = datetime.now().strftime("%Y%m%d") + ".log"

        if to == "stdout":
            handlers = [logging.StreamHandler(sys.stdout)]

        elif to == "file":
            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir)
            handlers = [logging.FileHandler(os.path.join(logs_dir, log_file_name))]

        else:
            handlers = [
                logging.StreamHandler(sys.stdout),
                logging.FileHandler(os.path.join(logs_dir, log_file_name)),
            ]

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)s | %(message)s",
            handlers=handlers,
        )

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"{func.__name__}: args: {args}, kwargs: {kwargs}")
            return func(*args, **kwargs)

        return wrapper

    return _logger

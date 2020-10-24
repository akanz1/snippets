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
import sys
from datetime import datetime
from pathlib import Path


def logger(to: str = "stdout", level: str = "info"):
    """Logging decorator.

    Example:
    @logger(to="both", level="warning")
    def func(x, y):
        return x + y

    Parameters
    ----------
    to : str, optional
        Specify the logging destinaton, by default "stdout"
        * "stdout", outputs to stdout
        * "file", logs to logs/YYYYmmdd.log
        * "both", logs to both

    level : str, optional
        Specify the logging level, by default "info"
    """

    def _logger(func):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logs_dir = "logs"
        log_file_name = datetime.now().strftime("%Y%m%d") + ".log"

        stream_handler = logging.StreamHandler(sys.stdout)
        file_handler = logging.FileHandler(Path(logs_dir, log_file_name))

        if to == "stdout":
            handlers = [stream_handler]

        elif to == "file":
            Path(logs_dir).mkdir(parents=True, exist_ok=True)
            handlers = [file_handler]

        elif to == "both":
            Path(logs_dir).mkdir(parents=True, exist_ok=True)
            handlers = [
                stream_handler,
                file_handler,
            ]

        else:
            raise ValueError(
                "Please specify a valid logging destination. ('stdout', 'file', 'both')"
            )

        logging.basicConfig(
            format="%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)s | %(message)s",
            handlers=handlers,
            level=level.upper(),
        )

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            getattr(logging, level.lower())(
                f"{func.__name__}(*{args}, **{kwargs}) | Output: {type(func(*args, **kwargs))}"
            )
            return func(*args, **kwargs)

        return wrapper

    return _logger

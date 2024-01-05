
from time import perf_counter
from typing import Callable
import functools
from logging_helper import Logger

def display_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        print('Time: {:.2} s'.format(t2 - t1))
        return result
    return wrapper



def benchmark(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        # 執行function
        res = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {run_time:.4f} seconds")
        return res
    return wrapper


def benchmark_with_logger(logger: Logger) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = perf_counter()
            # 執行function
            res = func(*args, **kwargs)
            end_time = perf_counter()
            run_time = end_time - start_time
            logger.log("info", f"Function {func.__name__}{args} {kwargs} Took {run_time:.4f} seconds")
            return res

        return wrapper

    return decorator




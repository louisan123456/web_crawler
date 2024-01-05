
import sys
sys.path.append(r'D:\brady\python\package')

import traceback
import functools
from typing import Callable
from logging_helper import Logger



traceback_printed = True

def log_factory(logger: Logger) -> Callable:
    def decorator(func):
        """
        Decorator provides simple exception handler: logs exception and throws it up
        :param
            func: Callable Function
            logger: Logger Class
        :return: inner func or exception
        """
        @functools.wraps(func)
        def inner(*args, **kwargs):
            # global config
            global traceback_printed
            try:
                res = func(*args, **kwargs)
                logger.log("info", "{} end".format(func.__name__))
            except Exception as e:
                if traceback_printed:
                    logger.log("error", "{} {}. \ntraceback: {}".format(func.__name__, e, traceback.format_exc()))
                else:
                    logger.log("error", "{} {}".format(func.__name__, e))
                raise e
            return res
    
        return inner
    
    return decorator


# @log_factory(logger)
# def f(x):
#     return x + 1

# f('1')
# f.__name__
# f.__module__
# f.__qualname__

# __name__
# x = Logger('n')


# logging_helper.__name__








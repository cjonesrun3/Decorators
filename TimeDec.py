import functools
from timeit import default_timer as timer

def timing_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = timer()
        value = func(*args, **kwargs)
        end = timer()
        delta = end - start

        message_to_user = 'Total elapsed time for {} is {}'.format(func.__name__, delta)
        print(message_to_user)
        return value
    return inner

@timing_decorator
def testing_with_range():
    for i in range(1, 10000):
        print(i)

testing_with_range()





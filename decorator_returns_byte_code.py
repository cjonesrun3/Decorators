import functools
import dis


def see_byte_code(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('Byte-Code for {}'.format(func.__name__))
        dis.dis(func)  # Returns byte-code for wrapped function
        value = func(*args)
        return value
    return inner

@see_byte_code
def greeting():
    print('Hello World')

greeting()

import functools


def printable_vars(func):
    @functools.wraps(func)
    def inner(*args):
        print('Function: ' + func.__name__ + ' was run')
        print('Function stated purpose: ' + func.__doc__)
        print('-' * 40)
        print('{:>10s}{:>20s}'.format('RECEIVED ARGUMENT', 'DATA TYPE'))
        print('-' * 40)
        for item in args:
            print('{:>10s}{:>30s}'.format(str(item), str(type(item))))
        print('-' * 40)
        value = func(*args)
        print('Function: ' + func.__name__ + ' has completed')

        return value
    return inner



@printable_vars
def addition(x, y, z):
    """
    I add three ints together

    """
    print(x + y + z)

print(addition(3, 10, 3))
import functools


class type_check:
    def __init__(self, t):
        self.t = t

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not all(map(lambda x, y: isinstance(x, y), args, self.t)):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper


if __name__ == '__main__':

    @type_check([int, int])
    def add(a, b):
        return a + b


    try:
        print(add(1, '2'))
    except Exception as error:
        print(type(error))

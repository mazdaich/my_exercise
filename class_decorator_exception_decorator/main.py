import functools


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs), None
        except Exception as e:
            return None, type(e)


if __name__ == '__main__':

    @exception_decorator
    def func(x):
        return 2 * x + 1

    print(func(1))
    print(func('bee'))

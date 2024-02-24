import functools


class ignore_exception:
    def __init__(self, *args):
        self.lst = [i for i in args]

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as e:
                if type(e) in self.lst:
                    print(f'Исключение {type(e).__name__} обработано')
                else:
                    raise e

        return wrapper


if __name__ == '__main__':

    @ignore_exception(ZeroDivisionError, TypeError, ValueError)
    def func(x):
        return 1 / x

    func(0)

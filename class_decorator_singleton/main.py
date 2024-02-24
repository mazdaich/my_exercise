def singleton(cls):
    cls._instance = None

    def new_new(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    old = cls.__new__
    cls.__new__ = new_new
    return cls


if __name__ == '__main__':
    @singleton
    class MyClass:
        pass


    obj1 = MyClass()
    obj2 = MyClass()

    print(obj1 is obj2)

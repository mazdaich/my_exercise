from abc import ABC, abstractmethod


class Validator():
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __set__(self, obj, val):
        self.validate(val)
        obj.__dict__[self._attr] = val

    def __get__(self, obj, attr):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]

    @abstractmethod
    def validate():
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self._minvalue = minvalue
        self._maxvalue = maxvalue

    def validate(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')

        if self._minvalue != None and val < self._minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self._minvalue}')

        if self._maxvalue != None and val > self._maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self._maxvalue}')


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self._minsize = minsize
        self._maxsize = maxsize
        self._predicate = predicate

    def validate(self, val):
        if not isinstance(val, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')

        if self._minsize != None and len(val) < self._minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self._minsize}')

        if self._maxsize != None and len(val) > self._maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self._maxsize}')

        if self._predicate and val:
            if not self._predicate(val):
                raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')


if __name__ == '__main__':

    class Student:
        age = Number(18, 99)


    student = Student()
    student.age = 19
    print(student.age)

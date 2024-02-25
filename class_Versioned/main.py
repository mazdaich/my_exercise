class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr
        cls._count = 1

    def __set__(self, obj, val):
        obj.__dict__[self._attr] = val
        obj.__dict__[obj._count] = val
        obj._count += 1

    def __get__(self, obj, attr):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def get_version(self, obj, n):
        return obj.__dict__[n]

    def set_version(self, obj, n):
        obj.__dict__[self._attr] = obj.__dict__[n]


if __name__ == '__main__':
    class Student:
        age = Versioned()

    student = Student()

    student.age = 18
    student.age = 19
    student.age = 20

    print(student.age)
    print(Student.age.get_version(student, 1))
    print(Student.age.get_version(student, 2))
    print(Student.age.get_version(student, 3))

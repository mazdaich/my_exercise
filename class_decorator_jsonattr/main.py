import json


def jsonattr(fn):
    def s(cls):
        with open(fn, 'r') as file:
            for k, v in json.load(file).items():
                setattr(cls, k, v)
            return cls
    return s


if __name__ == '__main__':

    with open('test.json', 'w') as file:
        file.write('{"name": "Кемаль", "breed": "Британский"}')

    @jsonattr('test.json')
    class Cat:
        def __init__(self, name=None, breed=None):
            self.name = name or self.name
            self.surname = breed or self.breed

    cat = Cat()
    print(cat.name)
    print(cat.breed)

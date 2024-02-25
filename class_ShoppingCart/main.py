class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, it=[]):
        self.lst = []
        for i in it:
            self.lst.append([i.name, i.price])

    def __str__(self):
        l = []
        for i in self.lst:
            l.append(f'{i[0]}, {i[1]}$')
        return '\n'.join(l)

    def add(self, t):
        self.lst.append([t.name, t.price])

    def total(self):
        return sum([x[1] for x in self.lst])

    def remove(self, t):
        for i in self.lst:
            if t in i:
                del self.lst[self.lst.index(i)]


if __name__ == '__main__':

    shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])

    shopping_cart.remove('Yoga Mat')
    print(shopping_cart)
    print(shopping_cart.total())

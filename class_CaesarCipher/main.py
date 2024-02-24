class CaesarCipher:
    def __init__(self, n):
        self.n = n
        self.lst = [chr(i) for i in range(97, 123)]
        self.txt = ''

    def encode(self, txt):
        self.txt = ''
        for i in txt:
            if 122 >= ord(i.lower()) + self.n >= 97 and i.lower() in self.lst:
                self.txt += chr(ord(i) + self.n)

            elif ord(i.lower()) + self.n > 122 and i.lower() in self.lst:
                self.txt += chr(ord(i) - 26 + self.n)
            else:
                self.txt += i
        return self.txt

    def decode(self, txt):
        self.txt = ''
        for i in txt:
            if 122 >= ord(i.lower()) - self.n >= 97 and i.lower() in self.lst:
                self.txt += chr(ord(i) - self.n)

            elif ord(i.lower()) - self.n < 97 and i.lower() in self.lst:
                self.txt += chr(ord(i) + 26 - self.n)

            else:
                self.txt += i
        return self.txt

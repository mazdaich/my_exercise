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


if __name__ == '__main__':
    cipher = CaesarCipher(10)

    words = ['leader', 'life', 'central', 'whatever', 'true', 'show', 'year', 'teacher', 'happen', 'might', 'defense',
             'suggest', 'boy', 'trip', 'wish', 'interest', 'star', 'system', 'husband', 'wait', 'young', 'certainly',
             'with', 'wind', 'thought', 'hard', 'today', 'cup', 'where', 'fly', 'agreement', 'human', 'decision',
             'along',
             'billion', 'prevent', 'authority', 'those', 'do', 'perform', 'plan', 'allow', 'president', 'do', 'around',
             'seven', 'dog', 'sea', 'use', 'my', 'head', 'whose', 'important', 'top', 'current', 'east', 'page',
             'decide',
             'mouth', 'whatever', 'hospital', 'pattern', 'smile', 'probably', 'at', 'evening', 'current', 'local',
             'want',
             'foreign', 'catch', 'option', 'meeting', 'course', 'collection', 'street', 'make', 'economic', 'fly',
             'return',
             'experience', 'east', 'position', 'foot', 'one', 'mean', 'break', 'me', 'truth', 'management', 'want',
             'option', 'economic', 'response', 'attorney', 'table', 'push', 'travel', 'water', 'help']

    encode_words = [cipher.encode(word) for word in words]
    print(encode_words)

    decode_words = [cipher.decode(word) for word in encode_words]
    print(decode_words)

from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in ['♣', '♢', '♡', '♠']
                     for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]

    def shuffle(self):
        if len(self.deck) != 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self.deck)

    def deal(self):
        try:
            return self.deck.pop()
        except:
            raise ValueError('Все карты разыграны')

    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'


if __name__ == '__main__':

    deck = Deck()

    print(deck)
    print(deck.deal())
    print(deck.deal())
    print(deck.deal())
    print(type(deck.deal()))
    print(deck)

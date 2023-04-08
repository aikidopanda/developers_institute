import random
cardvalues = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def show(self):
        print(f'{self.value} of {self.suit}')
class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build()
    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in cardvalues:
                self.cards.append(Card(s, v))
    def showcards(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r] , self.cards[i]
    def deal(self):
        return self.cards.pop()

    

#Testing
deck = Deck()
deck.shuffle()
card = deck.deal()
card.show()
# deck.showcards()
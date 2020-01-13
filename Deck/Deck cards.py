import random


class Deck:
    def __init__(self):
        colors = ["r", "b", "g", "y"]
        self.cards = [[i + 1, c] for i in range(10) for c in colors]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(len(self.cards) - 1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            raise StopIteration


if __name__ == '__main__':
    mydeck = Deck()
    for card in mydeck:
        print(card)
    if mydeck:
        card = mydeck.deal()
        print(card)
    else:
        print("the deck is empty")


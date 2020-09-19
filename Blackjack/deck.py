class deck:

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        suits = ["spades", "clubs", "diamonds", "hearts"]
        for suit in suits:
            for i in range(14): # 0 = ace, 11 = jack ... 13 = king
                self.cards.append(card(i,suit))


    def shuffle(self):
        pass

    def split(self, location):
        pass

    def take(self):
        pass

    def print(self):
        for card in self.cards:
            print(card)


class card:

    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __repr__(self):
        return "%s___%d" % (self.suit, self.num)

if __name__ == "__main__":
    deck1 = deck()
    deck1.print()

import random

def ShuffleList(list):
    firstHalf = list[:len(list)//2]
    secondHalf = list[len(list)//2:]
    list = []
    while len(firstHalf) and len(secondHalf):
        if random.randint(0,1):
            list.append(firstHalf.pop())
        else:
            list.append(secondHalf.pop())
    return list + firstHalf + secondHalf



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
        self.cards = ShuffleList(self.cards)
        self.cards = ShuffleList(self.cards)
        self.cards = ShuffleList(self.cards)
        self.cards = ShuffleList(self.cards)

    def split(self, location):
        self.cards = self.cards[location:] + self.cards[:location]

    def take(self):
        pass

    def print(self):
        print(self.cards)


class card:

    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __repr__(self):
        return "%s___%d" % (self.suit, self.num)

if __name__ == "__main__":
    deck1 = deck()
    deck1.print()
    deck1.shuffle()
    deck1.print()
    deck1.split(20)
    deck1.print()

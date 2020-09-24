from deck import *

def CheckWinner(playerCards, aiCards):
    playerTotal = 0
    for card in playerCards:
        if card.num == 0:
            playerTotal += 11
        elif card.num > 10:
            playerTotal += 10
        else:
            playerTotal += card.num
    if playerTotal > 21:
        for card in playerCards:
            if card.num == 0:
                playerTotal -= 10
            if card.num < 22:
                break
        if card.num > 21:
            return 0 # returns player lost
    aiTotal = 0
    for card in aiCards:
        if card.num == 0:
            aiTotal += 11
        elif card.num > 10:
            aiTotal += 10
        else:
            aiTotal += card.num
    if aiTotal > 21:
        for card in aiCards:
            if card.num == 0:
                aiTotal -= 10
            if card.num < 22:
                break
        if card.num > 21:
            return 1 # returns player won
    if aiTotal == playerTotal:
        return 2 # returns draw
    elif aiTotal > playerTotal:
        return 1
    else:
        return 0



if __name__ == "__main__":
    command = ''
    print("Welcome to Blackjack!")
    deck = deck()
    deck.shuffle()
    deck.split(int(input("Enter in a number 0-51 to split the deck: ")))
    
    while 1: # infinite game loop
        print("Your cards:")
        ownCards = []
        dealerCards = []
        ownCards.append(deck.take())
        ownCards.append(deck.take())
        while 1:
            print(ownCards)
            print("Enter H for hit, S for stand, of Q for quit:")
            command = input()
            print()
            if command.lower().strip() == 'q':
                break
            elif command.lower().strip() == 's':
                break
            elif command.lower().strip() == 'h':
                ownCards.append(deck.take())
        if command.lower().strip() == 'q':
            break

    print("Thanks for playing!")


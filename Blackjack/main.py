if __name__ == "__main__":
    print("Welcome to Blackjack!")
    
    while 1: # infinite game loop
        print("Enter H for hit, S for stand, of Q for quit:")
        command = input()
        print()
        if command.lower() == 'q':
            break

    print("Thanks for playing!")


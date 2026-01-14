#! python
import cardslib
import time
deck = cardslib.deck()
deck.shuffle()
def suit(int):
    match (int):
        case (0):
            return "Hearts"
        case (1):
            return "Diamonds"
        case (2):
            return "Clubs"
        case (3):
            return "Spades"
        case _:
            return "Unknown (This is a bug)"
def value(int):
    match(int):
        case(11):
            return "Jack"
        case(12):
            return "Queen"
        case(13):
            return "King"
        case(1):
            return "Ace"
        case _:
            return str(int)
def mainloop():
    print('d to draw a new card, s to shuffle, q, "quit" or leave blank to exit')
    userinput = input()
    match (userinput):
        case ("d"):
            card = deck.draw()
            if card == None:
                print("No cards left in the deck! Shuffle.")
            else:
                print("\033c", end="")
                print(f"You drew the {value(card.value)} of {suit(card.suit)}. {len(deck.cards) - deck.index} cards left in the deck")
        case ("s"):
            time.sleep(0.5)
            deck.shuffle()
            print("Shuffled")
        case ("q"):
            exit()
        case ("quit"):
            exit()
        case (""):
            exit()
        case _:
            print(f"Unrecognized command: '{userinput}'")
while True:
    mainloop()
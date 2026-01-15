from defaultdeck import defaultcards
import random
class card:
    def __init__(self, value: int, suit: int):
        """
        Initializes a card
        Args:
        Value: int
            Face cards (jack, queen, etc.) are represented as numbers over 10 (i.e. jack = 11, queen = 12, etc.)
        Suit: int 0-3
            0: Hearts
            1: Diamonds
            2: Clubs
            3: Spades
        Decks should be defined in a seperate file, importing this function. See defaultdeck for example
        """
        if not (0 <= suit <= 3): raise IndexError("Suit index out of range (0-3)")
        self.value = value
        self.suit = suit
        pass
    pass
class deck:
    """
    Class for a simulated deck of cards
    Methods: 
    draw(): Draw the next card in the deck
    shuffle(): Randomize 
    Decks are not randomized on initialization, call shuffle() when needed.
    Shuffling the deck returns it to its default state and sets index to 0. Cards that have been "used" are reshuffled back into the deck.
    """
    def __init__(self, cards:list = defaultcards, index: int = 0):
        """
        Creates a new deck.
        """
        self.cards = cards
        self.index = 0
        pass
    def shuffle(self):
        """
        Shuffles the deck randomly
        """
        random.shuffle(self.cards)
        self.index = 0
        pass
    def draw(self):
        """
        Draw cards from the deck.
        Returns a card object if there are cards left (see defaultdeck.py), otherwise returns None.
        """
        try:
            temp = self.cards[self.index]
            self.index = self.index + 1
            return temp
        except:
            return None
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
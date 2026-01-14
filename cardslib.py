from defaultdeck import defaultcards
import random

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
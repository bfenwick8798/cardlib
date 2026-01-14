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
defaultcards = [card(1, 0),card(2,0),card(3,0),card(4,0),card(5,0),card(6,0),card(7,0),card(8,0),card(9,0),card(10,0),card(11,0),card(12,0),card(13,0),card(1, 1),card(2,1),card(3,1),card(4,1),card(5,1),card(6,1),card(7,1),card(8,1),card(9,1),card(10,1),card(11,1),card(12,1),card(13,1),card(1, 2),card(2,2),card(3,2),card(4,2),card(5,2),card(6,2),card(7,2),card(8,2),card(9,2),card(10,2),card(11,2),card(12,2),card(13,2),card(1, 3),card(2,3),card(3,3),card(4,3),card(5,3),card(6,3),card(7,3),card(8,3),card(9,3),card(10,3),card(11,3),card(12,3),card(13,3)]
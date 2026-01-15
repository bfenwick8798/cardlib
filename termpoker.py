import cardslib as cards
import argparse
parser = argparse.ArgumentParser(
    prog='poker for bots'
)
#preamble
class player:
    """
    Player class
    id: int 
    name: str
    hand: list of 2 card objects, see cardslib
    points: 1000
    """
    def __init__(self, id: int, name: str, hand: list):
        self.id = id
        self.name = name
        self.hand = hand 
        self.points = 1000
        pass
    pass
parser.add_argument('playercount', type = int, default=4)
args = parser.parse_args()
if args.playercount < 2: 
    raise ValueError("you need multiple players to play the game.")
if args.playercount > 8:
    raise ValueError("only 8 players are allowed")


#functions
def parsecardstr(card: cards.card):
    return(f"{cards.value(card.value)} of {cards.suit(card.suit)}")
    pass   

#setting up the game
playernum = args.playercount 
deck = cards.deck()
deck.shuffle()
players = list()
#for i in range (playernum):
#        players.append(player(i,input(f"Input name of player {i + 1}: "),[]))
#commented out for testing 
for i in range (playernum):
       players.append(player(i,i,[]))
#players "draw" cards
for player in players:
    player.hand.append(deck.draw())
    player.hand.append(deck.draw())
    pass
#in-progress debugging stuff
#print(players)
#for player in players:
#    pass
#    print(f"Player {player.name}, with {player.points} points has a hand of {player.hand[1].value} {player.hand[1].suit}, {player.hand[0].value} {player.hand[0].suit}")
#main game loop
while True: #One loop is one round, consisting of 4 rounds
    pot = 0
    callamount = 0
    folded = []
    for player in players:
        tmpinput = ""
        print("\033c") # ANSI escape code for clear terminal
        bet = 0
        if player.id in folded:
            pass
        else:
            print(f"Player {player.id + 1} ({player.name})'s turn.")
            input("Press enter to begin turn...")
            print(f"Cards: {parsecardstr(player.hand[0])}, {parsecardstr(player.hand[1])}")
#            print(parsecardstr(player.hand[0]))
#            print(parsecardstr(player.hand[1]))
            print(f"You have {player.points} points.")
            if callamount == 0:
                exit = True
                while exit:
                    print("F to fold, R to bet or C to check.")
                    tmpinput = input("").upper()
                    match tmpinput:
                        case "F":
                            folded.append(player.id)
                            print("You folded.")
                            break
                        case "R":
                            while exit:
                                
                                bet = int(input("Enter how many points you would like to bet."))
                                try:
                                    if bet == player.points:
                                        print(f"You went all in for {player.points} points.")
                                        pot = pot + bet
                                        callamount = bet
                                        player.points = 0
                                        exit = False
                                    elif bet > player.points:
                                        print("You can't bet more points than you have!")
                                    else:
                                        print(f"You bet {bet} points.")
                                        player.points = player.points - bet
                                        callamount = bet
                                        pot = pot + bet
                                        exit = False
                                except:
                                    print("That wasn't a valid amount of points.")
                                finally:
                                    break
                        case "C":
                            print("You checked.")
                            exit = False
                        case _:
                            print("Invalid command.")
            else:
                exit = True
                while exit:    
                    print(f"F to fold, R to raise or C to call {callamount}.")
                    tmpinput = input("").upper()
                    match tmpinput:
                        case "F":
                            folded.append(player.id)
                            print("You folded.")
                            input("Press enter to continue...")
                            exit = False
                        case "R":
                            while exit:
                                bet = int(input("Enter how many points you would like to bet."))
                                try:
                                    if bet == player.points:
                                        print(f"You went all in for {player.points} points.")
                                        pot = pot + bet
                                        callamount = bet
                                        player.points = 0
                                        input("Press enter to continue...")
                                        exit = False
                                    elif bet > player.points:
                                        print("You can't bet more points than you have!")
                                    elif bet < callamount:
                                        print(f"Bet has to be above or equal to {callamount}")
                                    else:     
                                        print(f"You bet {bet} points.")
                                        player.points = player.points - bet
                                        callamount = bet
                                        pot = pot + bet
                                        input("Press enter to continue...")
                                        exit = False
                                except:
                                    print("That wasn't a valid amount of points.")
                        case "C":
                            print(f"You called. You put {callamount} points into the pot.")
                            player.points = player.points - callamount
                            pot = pot + callamount
                            input("Press enter to continue...")
                            break 
                        case _:
                            print("Invalid command.")

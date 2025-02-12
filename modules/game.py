from modules.card import Card
from modules.deck import Deck
from modules.player import HumanPlayer, Dealer

class Game:
    

    def __init__(self):
        self.nPlayers: int = 0
        self.Players: list[HumanPlayer] = []
        self.dealer: Dealer = Dealer()
        self.deck: Deck = Deck(1)

        self.turn = 0
        self.bettingTime = False
    

    def addPlayer(self, name):
        player: HumanPlayer = HumanPlayer(name, money=1000)
        self.Players.append(player)
    

    def deal(self, player):
        player.hand.addCard(self.deck.draw())


    def new_game(self):
        self.card_width = round(-35/36 * (len(self.Players) -1) **2 + 105)

        for i in range(2):
            for p in self.Players:
                self.deal(p)
            self.deal(self.dealer)
        
        self.bettingTime = True
    

    def playerBet(self, player, bettedAmount):

        player.bet = bettedAmount

        for p in self.Players:
            if p.bet == 0:
                print("pass")
                break
            #modificaprint("stop")
            self.bettingTime = False
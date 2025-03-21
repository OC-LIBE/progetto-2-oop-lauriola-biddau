from modules.card import Card
from modules.deck import Deck
from modules.player import HumanPlayer, Dealer

class Game:
    

    def __init__(self):
        self.nPlayers: int = 0
        self.Players: list[HumanPlayer] = []
        self.dealer: Dealer = Dealer()
        self.deck: Deck = Deck(1)

        self.namesGiven = False
        self.bettingTime = False
        self.playersDone = False
        self.dealerDone = False


    def addPlayer(self, name):
        player: HumanPlayer = HumanPlayer(name, money=1000)
        self.Players.append(player)
    

    def deal(self, player):
        player.hand.addCard(self.deck.draw())


    def new_game(self):  # before betting
        self.namesGiven = True
        self.card_width = round(-35/36 * (len(self.Players) -1) **2 + 105)
        self.bettingTime = True
    

    def playerBet(self, player, bettedAmount):  # during betting

        player.bet = bettedAmount
        player.money -= bettedAmount

        bets = 0
        for p in self.Players:
            if p.bet != 0:
                bets += 1
        
        if bets == len(self.Players):
            self.bettingTime = False
            
            for i in range(2):
                for p in self.Players:
                    self.deal(p)
                self.deal(self.dealer)
    

    def playerHit(self, plr):
        self.deal(plr)
    

    def playerStand(self, plr):
        plr.stood = True
    

    def dealerTurn(self):
        self.playersDone = True
        if self.dealer.busted == False:
            pass
    

    def checkWins(self):
        """
        for plr in self.Players:

            win = False
            bj = False
            tie = False

            if self.dealer.busted == True:

                if plr.busted == False:

                    if plr.hand.score[0] == 21 or plr.hand.score[1] == 21 and len(plr.hand.cards) == 2:
                        bj = True

                    else:
                        win = True
            else:
                
                if plr.busted == False:

                    if (plr.hand.score[0] == 21 or plr.hand.score[1] == 21) and len(plr.hand.cards) == 2:
                        if self.dealer.hand.score[0] == 21 or self.dealer.hand.score[1] == 21 and len(self.dealer.hand.cards) == 2:
                            
                            tie = True
                        
                        else:
                            bj = True
                    
                    else:
                        for sum in plr.hand.score:
                            if sum <= 21:
                                if self.dealer.hand.score[0] <= 21:
                                    if sum > self.dealer.hand.score[0]:
                                        
                                        if self.dealer.hand.score[1] <= 21:
                                            if sum > self.dealer.hand.score[1]:
                                                win = True
        """
        
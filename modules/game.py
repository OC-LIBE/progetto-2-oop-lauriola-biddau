from modules.deck import Deck
from modules.player import HumanPlayer, Dealer

class Game:

    def __init__(self):
        self.nPlayers: int = 0
        self.Players: list[HumanPlayer] = []
        self.dealer: Dealer = Dealer()

        self.namesGiven = False
        self.nDecks = 0
        self.bettingTime = False
        self.playersDone = False
        self.dealerDone = False
        self.gameDone = False


    def addPlayer(self, name):
        player: HumanPlayer = HumanPlayer(name, money=1000.0)
        self.Players.append(player)
    

    def deal(self, player):
        player.hand.addCard(self.deck.draw())


    def new_game(self):  # before betting
        self.namesGiven = True
        self.deck: Deck = Deck(self.nDecks)
        self.deck.shuffle()
        self.bettingTime = True
    

    def playerBet(self, player, bettedAmount):  # during betting
        player.bet = bettedAmount
        
    
    def dealIfBetsOver(self):
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
    

    def checkBj(self, plr) -> bool:
        if plr.hand.score == 21 and len(plr.hand.cards) == 2:
            return True
        else:
            return False
    

    def playerHit(self, plr):
        self.deal(plr)
    

    def playerStand(self, plr):
        plr.stood = True
    

    def doubleDown(self, plr):
        self.deal(plr)
        plr.bet *= 2
        if plr.bet > plr.money:
            plr.bet = plr.money

        plr.doubleDown = True


    def dealerTurn(self):
        self.playersDone = True
        if self.dealer.busted == False:
            
            if self.dealer.hand.score < 17:
                self.deal(self.dealer)
            else:
                self.dealer.stood = True
                self.dealerDone = True
        
        else:
            self.dealerDone = True
    

    def checkWins(self):

        for plr in self.Players:

            
            if self.dealer.busted == True:

                if plr.busted == False:
                    if plr.hand.score == 21 and len(plr.hand.cards) == 2:
                        plr.outcome = "bj"
                    else:
                        plr.outcome = "win"

                else:
                    plr.outcome = "loss"
            else:

                if plr.busted == True:
                    plr.outcome = "loss"
                else:

                    if self.dealer.hand.score == 21 and len(self.dealer.hand.cards) == 2:
                        
                        if plr.hand.score == 21:
                            if len(plr.hand.cards) == 2:

                                plr.outcome = "tie"
                            else:
                                plr.outcome = "loss"
                        else:
                            plr.outcome = "loss"

                    else:

                        if plr.hand.score == 21 and len(plr.hand.cards) == 2:
                            plr.outcome = "bj"
                        
                        else:
                            if plr.hand.score > self.dealer.hand.score:
                                plr.outcome = "win"

                            elif plr.hand.score == self.dealer.hand.score:
                                plr.outcome = "tie"

                            else:
                                plr.outcome = "loss"

            if plr.outcome == "bj":
                plr.money += 1.5 * plr.bet
                
            elif plr.outcome == "win":
                plr.money += 1 * plr.bet

            elif plr.outcome == "tie":
                plr.money += 0 * plr.bet
            
            elif plr.outcome == "loss":
                plr.money += -1 * plr.bet
                
        
        self.gameDone = True
    

    def restart(self):
        self.deck = Deck(self.nDecks)
        self.deck.shuffle()

        self.bettingTime = True
        self.playersDone = False
        self.dealerDone = False
        self.gameDone = False

        plrsToRemove = []
        for plr in self.Players:

            if plr.money < 50:
                plrsToRemove.append(plr)
        
        for plr in plrsToRemove:
            self.Players.remove(plr)
        
        if len(self.Players) > 0:
        
            for plr in self.Players:
                plr.stood = False
                plr.doubleDown = False
                plr.hand.cards = []
                plr.bet = 0
                plr.outcome = ""

            self.nPlayers = len(self.Players)
            self.dealer = Dealer()
        
        else:
            self.__init__()

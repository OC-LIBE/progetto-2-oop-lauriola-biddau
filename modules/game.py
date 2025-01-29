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
    
    def addPlayer(self, name) -> HumanPlayer:
        player: HumanPlayer = HumanPlayer(name, money=1000)
        self.Players.append(player)
    
    def deal(self, player) -> list[Card]:
        pass

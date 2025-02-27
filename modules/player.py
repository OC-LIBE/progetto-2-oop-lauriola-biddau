import modules.card as Card

class Player:

    def __init__(self):

        self.hand = self.Hand()
        self.stood: bool = False


    @property
    def busted(self):
        if self.hand.score[0] > 21 and self.hand.score[1] > 21:
            return True
        else:
            return False


    class Hand:
        
        def __init__(self):

            self.cards: list = []
        
        def addCard(self, card: Card):
            self.cards.append(card)  # no need to remove the card, because deck.draw() already does
        
        @property
        def score(self):  # due somme perché gli assi possono avere due valori
            sum0 = 0
            sum1 = 0
            for card in self.cards:
                sum0 += card.card_scores[0]
                sum1 += card.card_scores[1]
            return [sum0, sum1]


class HumanPlayer(Player):

    def __init__(self, name, money):
        super().__init__()
        
        
        self.name: str = name
        self.money: float = money
        self.bet: int = 0
    

    def __repr__(self):
        return f"name: {self.name}, money: {self.money}, cards: {self.hand.cards}, score: {self.hand.score[0]} or {self.hand.score[1]}, bet: {self.bet}, busted: {self.busted}, standing: {self.stood}"


class Dealer(Player):

    def __init__(self):
        super().__init__()
    

    def __repr__(self):
        return f"cards: {self.hand.cards}, score: {self.hand.score[0]} or {self.hand.score[1]} busted: {self.busted}, standing: {self.stood}"
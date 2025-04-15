import modules.card as Card

class Player:

    def __init__(self):

        self.hand = self.Hand()
        self.stood: bool = False


    @property
    def busted(self):
        if self.hand.score > 21:

            hasAce = False
            for i in self.hand.cards:
                if i.card_score == 11:
                    hasAce = True
                    i.card_score = 1
                    break
            
            if hasAce == False:
                return True
            else:
                return self.busted
        else:
            return False


    class Hand:
        
        def __init__(self):

            self.cards: list = []
        

        def addCard(self, card: Card):
            self.cards.append(card)  # no need to remove the card, because deck.draw() already does
        

        @property
        def score(self):
            sum = 0
            for card in self.cards:
                sum += card.card_score
            return sum


class HumanPlayer(Player):

    def __init__(self, name, money):
        super().__init__()
        
        
        self.name: str = name
        self.money: float = money
        self.bet: int = 0
        self.doubleDown: bool = False

        self.outcome: str = ""
    

    def __repr__(self):
        return f"name: {self.name}, money: {self.money}, cards: {self.hand.cards}, score: {self.hand.score}, bet: {self.bet}, busted: {self.busted}, standing: {self.stood}, double down: {self.doubleDown}, outcome: {self.outcome}"


class Dealer(Player):

    def __init__(self):
        super().__init__()
    

    def __repr__(self):
        return f"cards: {self.hand.cards}, score: {self.hand.score} busted: {self.busted}, standing: {self.stood}"

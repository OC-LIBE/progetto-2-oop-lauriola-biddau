class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        if self.rank == 1:
            self.card_score = 11
        elif self.rank >= 11 and self.rank <= 13:
            self.card_score = 10
        else:
            self.card_score = self.rank

        if self.rank == 1:
            self.short_rank = 'A'
        elif self.rank == 11:
            self.short_rank = 'J'
        elif self.rank == 12:
            self.short_rank = 'Q'
        elif self.rank == 13:
            self.short_rank = 'K'
        else:
            self.short_rank = str(self.rank)

        if self.suit == 'Spades':
            self.short_suit = 'S'
        elif self.suit == 'Hearts':
            self.short_suit = 'H'
        elif self.suit == 'Clubs':
            self.short_suit = 'C'
        else:
            self.short_suit = 'D'

        self.image_location = 'static/images/{}{}.png'.format(
            self.short_rank, self.short_suit)
    
    def __repr__(self):
        return f"{self.short_rank, self.short_suit}"
        
    @property
    def front_image(self):
        return self.image_location
    
    @property
    def back_image(self):
        return 'static/images/Back.png'

class Card(object):
    def __init__(self, suit, values):
        self.suit = suit
        self.values = values
    

class Deck(Card):
    def __init__(self, create, cards=[]):
        self.cards = cards
        self.create = create
        # self.shuffle = shuffle
        # self.retire = retire
        
    def create(self):
        suit = ["hearts", "diamonds", "clubs", "spades"]
        for i in range(len(suit)):
            for j in range(1,14):
                self.cards.append("{} of {}".format(j, suit[i]))
        print self.cards   
        return self     


class Player(object):
    def __init__(self, hand, name, discard, draw, show):
        self.hand = hand
        self.name = name
        self.discard = discard 
        self.draw = draw
        self.show = show

test = Deck()
test.create()
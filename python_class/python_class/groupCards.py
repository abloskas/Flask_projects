
class Card(object):
    def __init__(self, suit, values):
        self.suit = suit
        self.values = values
    def __str__(self):
        return "Suit: {} Value: {}".format(self.suit, self.values)
     
    

class Deck(Card):
    def __init__(self):
        self.cards = []

        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]

        for i in range(len(suits)):
            for x in range(len(values)):
                self.cards.append(Card(suits[i],values[x]))
              
    def show(self):
        for i in self.cards:
            print i
        return self    



vegasDeck = Deck()
vegasDeck.show()

class Player(object):
    def __init__(self, name, deck):
        self.hand = []]
        self.name = name
        


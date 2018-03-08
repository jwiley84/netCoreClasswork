####
#
#DECK CLASS
#list of cards
#be able to shuffle
#
#CARD CLASS
#
#
###


#### 
#CARD CLASS
###
import random


class Card(object):
    def __init__ (self, face, suit, id):
        self.face = face;
        self.suit = suit;
        self.id = id;

#testCard = Card("Jack", "Heart")

#print(testCard.face)

class Deck(object):
    def __init__(self):
        self.deckArr = [];
        self.createDeck();

    #create array of self.card 52 times
    def createDeck(self):
        faces = [2, 3]
        # 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"];
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for face in faces:
            for suit in suits: 
                card = Card(str(face), str(suit), (str(face)+suit))
                #print(card.id)
                self.deckArr.append(card)
        return self;

    #test deck
    def showDeck(self):
        for cardy in self.deckArr:
            print(cardy.id)

    #shuffle deck
    def shuffly(self):
        for cardsy in range(1, 53):
            randomizer = random.randint(1,52);
            print(randomizer)
    
mahDeck = Deck();

mahDeck.createDeck().showDeck();



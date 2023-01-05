class Card(object): #object is an identifier known as a base class
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "  "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []
        
    def add(self, card):
        self.cards.append(card)
        
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print ("Out of cards!")


def main():
    
    c1 = Card("A", "s")
    c2 = Card("K", "s")
    c3 = Card("J", "h")
    c4 = Card("Q", "d")

    print("c1: " + str(c1))
    print("c2: " + str(c2))
    print("c3: " + str(c3))
    print("c4: " + str(c4))

    #all will show "<empty>" if I did a print statement, but I printed John to show this
    Mary = Hand()
    John = Hand()
    print("John: " + str(John))
    Carl = Hand()
    Henry = Hand()

    #add method
    Mary.add(c1)
    Carl.add(c3)
    Henry.add(c4)
    print("Mary: " + str(Mary))
    print("Carl: " + str(Carl))
    print("Henry: " + str(Henry))

    #give method
    Mary.give(c1, John)
    print("Mary gave her card, current hand: " + str(Mary))
    print("John took her card, current hand: " + str(John))

    #Every hand in 1 list
    allHands = [Henry, Carl, John, Mary]

    deck1 = Deck()
    print()
    
    #populate method
    deck1.populate()
    print("Deck 1 populated: " + str(deck1))

    #shuffle method
    deck1.shuffle()
    print("Deck 1 shuffled: " + str(deck1))

    #deal method
    deck1.deal(allHands, per_hand = 2)
    print("All players draw 2 cards: \n")
    print("Henry: " +str(Henry))
    print("Carl: " + str(Carl))
    print("John: " + str(John))
    print("Mary: " + str(Mary))
    
    #clears a specific hand
    Henry.clear()
    print("Clearing Henry's hand: " + str(Henry))
    
main()

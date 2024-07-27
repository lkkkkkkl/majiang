from random import randint

SUIT_ORDER = {'万': 0, '条': 1, '筒': 2}

## 每一张牌
class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.suit_order = SUIT_ORDER[suit]
        self.value = value
    
    def __repr__(self):
        return f"{self.value}{self.suit}"
    
## 每一个人的手牌
class Hand():
    def __init__(self):
        self.cards = []
    
    def card_add(self, card):
        self.cards.append(card)
    
    def card_remove(self, card):
        self.cards.remove(card)
    
    def card_have(self, card):
        return card in self.cards
    
    def arrange_card(self):
        #card_changed = 
        card_suited = sorted(self.cards, key = lambda card :card.value)
        card_valued = sorted(card_suited, key = lambda card :card.suit_order)
        self.cards =  card_valued
        #print(card_valued)

# 
# 有定缺规则
class Person():
    def __init__(self, name):
        self.name    = name
        self.hand    = Hand()
        self.played  = []
        self.dropout = None
        #self.dropout_digit = 
    
    def draw_card(self, card):
        self.hand.card_add(card)

    def discard_card(self, card):
        self.hand.card_remove(card)
        self.played.append(card)

    def __repr__(self):
        return f"{self.name}"
    

class Game():
    def __init__(self, players):
        self.players = players
        self.deck    = self.create_deck()
        self.starter = self.players[self.starter_choose()]

    #开启牌局，生成牌
    def create_deck(self):
        deck = []
        for suit in ['筒', '条', '万']:
            for value in [i for i in range(1, 10)]:
                #card = 
                for i in range(4):
                    deck.append(Card(suit, value))
        return deck
    
    # 选出庄家
    def starter_choose(self):
        scores = []
        for player in self.players:
            scores.append(randint(1, 99))
        return scores.index(max(scores))
    
    # 发牌
    def distribute_card(self):
        """for round in range(12):
            i = self.players.index(self.starter)
            while True:
                card = self.deck.pop(randint(0,len(self.deck)-1))
                self.players[i].draw_card(card)
                if i == len(self.players):
                    i = 0"""
        for _ in range(12):
            for i in range(len(self.players)):
                card = self.deck.pop(randint(0,len(self.deck)-1))
                #print(card)
                starter_ith = self.players.index(self.starter)
                self.players[(starter_ith + i) % len(self.players)].draw_card(card)

        card = self.deck.pop(randint(0,len(self.deck)-1))
        self.starter.draw_card(card)


p1, p2, p3, p4 = Person('p1'), Person('p2'), Person('p3'), Person('p4')
game1 = Game([p1, p2, p3, p4])
#print(game1.deck, len(game1.deck))
game1.distribute_card()
for i in game1.players:
    i.hand.arrange_card()
print(game1.starter, game1.players)
for i in game1.players:
    print(i.hand.cards)
print(len(game1.deck))
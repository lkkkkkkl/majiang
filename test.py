from random import randint
from collections import Counter

SUIT_ALL = ['万', '条', '筒']
SUIT_ORDER = {'万': 0, '条': 1, '筒': 2}

## 每一张牌
class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.suit_order = SUIT_ORDER[suit]
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.value == other.value
        return False

    
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
        self.name     = name
        self.hand     = Hand()
        self.played   = []
        self.dropsuit = None # ('万', 3)
        self.deadcard = [] # 已经碰或杠的牌
        #self.dropout_digit = 
    
    # 摸牌
    def draw_card(self, card):
        self.hand.card_add(card)

    # 出牌
    def discard_card(self, card):
        self.hand.card_remove(card)
        self.played.append(card)

    # 用数量来定缺
    def drop_suit(self):
        #self.hand.cards.count()
        #counts = Counter(self.hand.cards.suit).most_common()
        counts = Counter()
        for i in self.hand.cards:
            counts[i.suit] += 1
        # 输出张数最少的
        # counts.most_common() 返回 从高到低的list
        # 函数返回定缺的花色
        return counts.most_common()[:1:-1][0][0]
        #return counts
    
    def return_drop(self):
        card_2drop = []
        for card in self.hand.cards:
            if card.suit == self.dropsuit:
                card_2drop.append(card)
        
        return card_2drop
    
    # 选择出的牌
    def choose_drop(self):
        pass

    
    def can_peng(self, card):
        if card.suit == self.drop_suit:
            return False
        if  self.hand.cards.count(card) >= 2:
            return True
        else:
            return False
    
    def peng(self, card):
        if self.can_peng(card):
            self.deadcard.append([card, 3])
            self.hand.cards.remove(card)
            self.hand.cards.remove(card)

    def can_gang(self, card, is_yourturn):
        if card.suit == self.drop_suit:
            return False
        # 在自己的回合摸到牌可以杠，只能是贴/暗杠
        if is_yourturn:
            if self.hand.cards.count(card) == 3:
                return True
            elif [card, 3] in self.deadcard :
                return True
            return False
        else:
            if self.hand.cards.count(card) == 3:
                return True
            else:
                return False
    
    def gang(self, card, is_yourturn):
        if self.can_gang(self, card, is_yourturn):
            if is_yourturn:
                if self.hand.cards.count(card) == 3:
                    for _ in range(3):
                        self.hand.card_remove(card)
                    self.deadcard.append([card, 4])
                elif [card, 3] in self.deadcard:
                    self.deadcard.remove([card, 3])
                    self.deadcard.append([card, 4])
            else:
                if self.hand.cards.count(card) == 3:
                    for _ in range(3):
                        self.hand.card_remove(card)
                    self.deadcard.append([card, 4])               
    
    def can_win(self, card, is_yourturn):
        
        pass

    def __repr__(self):
        return f"{self.name}"
    
"""P1 = Person('pp1')
card1 = Card('万', 1)
P1.hand.card_add(card1)
P1.hand.card_add(card1)
#P1.hand.card_add(card1)
print(P1.can_peng(card1))
P1.peng(card1)
print(P1.hand.cards, P1.deadcard, P1.can_gang(card1, False))"""


class Game():
    def __init__(self, players):
        self.players = players
        self.deck    = self.create_deck()
        self.starter = self.players[self.starter_choose()]
        self.remain_cards = 108

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
        """
        for round in range(12):
            i = self.players.index(self.starter)
            while True:
                card = self.deck.pop(randint(0,len(self.deck)-1))
                self.players[i].draw_card(card)
                if i == len(self.players):
                    i = 0
        """
        for _ in range(12):
            for i in range(len(self.players)):
                card = self.deck.pop(randint(0,len(self.deck)-1))
                #print(card)
                starter_ith = self.players.index(self.starter)
                self.players[(starter_ith + i) % len(self.players)].draw_card(card)
                self.remain_cards -= 1

        # 庄家开局多摸一张
        card = self.deck.pop(randint(0,len(self.deck)-1))
        self.starter.draw_card(card)
        self.remain_cards -= 1
    
    # 开始棋局
    def start_game(self):
        ith_person = self.players.index(self.starter)
        while len(self.deck) != 0 and len(self.players) != 1:
            current_player = self.players[ith_person]
            if len(self.deck) == 59:
                current_player.drop
            else:
                self.players[ith_person].get
                self.players[ith_person].drop

    




p1, p2, p3, p4 = Person('p1'), Person('p2'), Person('p3'), Person('p4')
game1 = Game([p1, p2, p3, p4])
#print(game1.deck, len(game1.deck))
game1.distribute_card()
for i in game1.players:
    i.hand.arrange_card()
print(game1.starter, game1.players)
for i in game1.players:
    for card in game1.deck:
        pass
        #print(card, i.can_pong(card), end=' ')
    print(i.hand.cards)
    #print(i.drop_suit())
print(len(game1.deck), game1.remain_cards)


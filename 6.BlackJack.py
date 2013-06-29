# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        s = ""	# return a string representation of a hand
        for item in self.hand:
            s += str(item) + " "
        return "Hand contains: " + s
        
        
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand
        
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0	# compute the value of the hand, see Blackjack video
        aces = 0
        for x in self.hand:
            if x.get_rank() == "A":
                aces += 1
            hand_value += VALUES[x.get_rank()]
        if aces == 0:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
                
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for x in self.hand:
            #card.draw(canvas,[0+CARD_SIZE*x + 10,300])
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(x.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(x.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + CARD_SIZE[0]*self.hand.index(x), pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for suit in range(0,4):
            rank = 0
            for rank in range(0,13):
                next_card = Card(SUITS[suit],RANKS[rank])
                self.deck.append(next_card)  

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()    # deal a card object from the deck
    
    def __str__(self):
        s = ""
        for i in self.deck:	# return a string representing the deck
            s += str(i) + " "
        return "Deck contains: " + s
                
#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    if in_play:
        score -= 1
        outcome = "Player loses! New Game. Hit or Stand?"
        return outcome
        
    # your code goes here
    deck = Deck()
    deck.shuffle()
    #print deck
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    #print "Player's",player_hand
    #print "Dealer's",dealer_hand
    
    outcome = "Hit or Stand?"
    in_play = True
   

def hit():
    global outcome, score, in_play
    player_hand.add_card(deck.deal_card())
    #print player_hand, player_hand.get_value()
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21:
        #print "You have Busted, dealer wins. New Deal?"
        outcome = "You have Busted, dealer wins. New Deal?"
        in_play = False
        score -= 1
        
def stand():
    global outcome, score, in_play
    if player_hand.get_value() > 21:
        #print "You have Busted, dealer wins. New Deal?"
        outcome = "You have Busted, dealer wins. New Deal?"
        score -= 1
        return score, outcome, in_play
     
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
            #print dealer_hand
        else:
            if dealer_hand.get_value() > 21:
                #print "Dealer has Busted, you win. New Deal?"
                outcome = "Dealer has Busted, you win. New Deal?"
                in_play = False
                score += 1
                return score, outcome, in_play
            elif player_hand.get_value() <= dealer_hand.get_value():
                #print "Dealer Wins! New Deal?"
                outcome = "Dealer Wins! New Deal?"
                in_play = False
                score -= 1
                return score, outcome, in_play
            else:
                #print "You Win! New Deal?"
                outcome = "You Win! New Deal?"
                score += 1
                in_play = False
                return score, outcome, in_play
        
        
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas, [0, 200])    
    player_hand.draw(canvas, [0, 400])
    canvas.draw_text("BlackJack",[200,75],50,"Black")
    canvas.draw_text("Score: " + str(score),[0,100],24,"Black")
    canvas.draw_text(outcome,[0,150],24,"Black")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_SIZE)
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
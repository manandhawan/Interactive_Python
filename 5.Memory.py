import simplegui
import random

def init():
    global list1,list2,deck,exposed,state,moves
    list1 = range(0,8)
    list2 = range(0,8)
    deck = list1 + list2
    random.shuffle(deck)
    exposed = [False for i in range(16)]
    state = 0
    moves = 0

def mouseclick(pos):
    global click,exposed,card1,card2,state,moves,value1,value2
    click = pos[0]//50
    if state == 0:
        if not exposed[click]:
            exposed[click] = True
            card1 = click
            value1 = deck[click]
            state = 1
    elif state == 1:
        if not exposed[click]:
            exposed[click] = True
            card2 = click
            value2 = deck[click]
            state = 2
            moves +=1
    elif state == 2:
        if not exposed[click]:
            if not value1 == value2:
                exposed[card1] = False
                exposed[card2] = False
            exposed[click] = True
            value1 = deck[click]
            card1 = click
            state = 1
 
def draw(canvas):
    global list1,list2,deck,exposed,card,moves
    label.set_text("Moves = " + str(moves))
    for card in range(len(deck)):
        if exposed[card]:
            canvas.draw_text(str(deck[card]),[10+50*card,60],50,"White")
        else:
            canvas.draw_polygon([[(card*50)+0, 0], [(card*50)+50, 0], [(card*50)+50, 100], [(card*50)+0, 100]], 4, "Black", "Green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

frame.start()
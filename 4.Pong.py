import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
score1 = 0
score2 = 0
ball_pos = [WIDTH/2,HEIGHT/2]
right = True




# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    if right == True:
        ball_vel = [random.randrange(120, 240)/60,-random.randrange(60, 180)/60]
    elif right == False:
        ball_vel = [-random.randrange(120, 240)/60,-random.randrange(60, 180)/60]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    ball_init(right)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,right,paddle1_vel,paddle2_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos <= (HALF_PAD_HEIGHT) and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle2_pos <= (HALF_PAD_HEIGHT) and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle1_pos >= (HEIGHT - (HALF_PAD_HEIGHT)) and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos >= (HEIGHT - (HALF_PAD_HEIGHT)) and paddle2_vel > 0:
        paddle2_vel = 0    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
        
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line([0,paddle1_pos - HALF_PAD_HEIGHT],[0,paddle1_pos + HALF_PAD_HEIGHT],16,"White")
    c.draw_line([WIDTH - PAD_WIDTH/2,paddle2_pos - HALF_PAD_HEIGHT],[WIDTH - PAD_WIDTH/2,paddle2_pos + HALF_PAD_HEIGHT],PAD_WIDTH,"White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] <= paddle1_pos - HALF_PAD_HEIGHT or ball_pos[1] >= paddle1_pos + HALF_PAD_HEIGHT:
            right = True
            ball_init(right)
            score2 += 1
        else:
            ball_vel[0] = -ball_vel[0]*1.1
    elif ball_pos[0] >= (WIDTH - 1 - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] <= paddle2_pos - HALF_PAD_HEIGHT or ball_pos[1] >= paddle2_pos + HALF_PAD_HEIGHT:
            right = False
            ball_init(right)
            score1 += 1
        else:
            ball_vel[0] = -ball_vel[0]*1.1
        
    
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    if score1 == 5 or score2 == 5:
        new_game()
    
    
    # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS,3,"Red","White")    
    c.draw_text(str(score1),(WIDTH/4,50),32,"White")
    c.draw_text(str(score2),(0.75*WIDTH,50),32,"White")
    
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 4
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0



# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game",new_game)
frame.add_label("5 points to win")




# start frame
frame.start()
new_game()

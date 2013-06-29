import simplegui
import random

num = 0
count = 0
count1 = 0


    
def range100():
    global num,count,count1
    count = 7
    count1 = 7
    num = random.randrange(0,100)
    print ""
    print "New Game.Range is from 0 to 100"
    print "Remaining number of Guesses: ", count
    print ""
    
def range1000():
    global num,count,count1
    count = 10
    count1 = 10
    num = random.randrange(0,1000)
    print ""
    print "New Game.Range is from 0 to 1000"
    print "Remaining number of Guesses: ", count
    print ""
    
def get_input(guess):
    global num,count
    value = int(guess)
    count -= 1
    if value < num:
        print "Guess was", value
        print "Remaining number of Guesses: ", count
        print "Higher!"
        print ""
    elif value > num:
        print "Guess was", value
        print "Remaining number of Guesses: ", count
        print "Lower!"
        print ""
    elif value == num:
        print "Guess was", value
        print "Guessed with %d Guesses" %(count1 - count)
        print "Correct!"
        range100()
    if count == 0:
        print ""
        print "You ran out of choices. The number was", num
        range100()
        
        
    

frame = simplegui.create_frame("Guess the Number",400,400)

frame.add_button("Range [0,100)",range100,200)
frame.add_button("Range [0,1000)",range1000,200)
frame.add_input("Enter your Guess",get_input,200)

range100()
frame.start()


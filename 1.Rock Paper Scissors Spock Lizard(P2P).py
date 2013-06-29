# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


def name_to_number(name):
    number = 0
    if name == 'rock':
        number = 0    
    elif name == 'spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name =='lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    return number


i = int(input("How many times do you want to play?"))

def rpsls(): 
    
    player_name1 = input("Player 1 Enter your choice:")
    player_name2 = input("Player 2 Enter your choice:")
    
    player_name1 = player_name1.lower()
    player_name2 = player_name2.lower()
    
    player_number1 = name_to_number(player_name1)
    player_number2 = name_to_number(player_name2)
    
    diff = (player_number1 - player_number2)%5
    
    l = ['rock','spock','paper','lizard','scissors']
    if player_name1 in l:
        if player_name2 in l:
            if diff == 0:
                print 'Player 1 chooses', player_name1
                print 'Player 2 choses', player_name2
                print "Player 1 and Player 2 tie!"
            elif diff == 1:
                print 'Player 1 chooses', player_name1
                print 'Player 2 choses', player_name2
                print "Player 1 wins!"
            elif diff == 2:
                print 'Player 1 chooses', player_name1
                print 'Player 2 choses', player_name2
                print "Player 1 wins!"
            elif diff == 3:
                print 'Player 1 chooses', player_name1
                print 'Player 2 choses', player_name2
                print "Player 2 wins!"
            elif diff == 4:
                print 'Player 1 chooses', player_name1
                print 'Player 2 choses', player_name2
                print "Player 2 wins!"
            else:
                print 'Choose a valid option!'
            print ''
        else:
            print 'Invalid Choice!'
            print ''
    else:
        print 'Invalid Choice!'
        print ''
    

while i > 0:
    rpsls()
    i = i - 1



#The game Rock Paper Scissors explained
#First import random so the computer can choose random between Rock, Paper and Scissors
#Define the variables: moves, player_wins, player_move, computer_move

#To create the possibility to stop, create a while loop (Boolean) with the q-value
#By compairing the values of player_move with computer_move, 
#Result will be tie, win of loose.
#This is possible by using the if, elif and else loop


import random

moves = ['r','p','s']
player_wins = ['pr','sp','rs']

print("Welcome to the game Rock, Paper Scissors!")
print("Choose between R, P or S:")
print ("q = quit")

while True:
    player_move=input("your move:")
    if player_move == str('q'):
        break
    computer_move=random.choice(moves)

    print ('You:', player_move)
    print ('Me computer:'  , computer_move)

    if player_move==computer_move:
        print('Tie')
        print ()

    elif player_move + computer_move in player_wins:
        print('You win!')
        print()
    else:
        print('You lose....')
        print()
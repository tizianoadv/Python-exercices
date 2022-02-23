""" Casino game - Russian roulette
    At the beginnning the player has a pot with 50 $ inside
    The player choose a number between 0 - 49
    Then he give his bet
        if the ball fall on the same number as the one chosen by the player, the user wins 3 times his bet
        Otherwise if the two numbers are even or odd then the player wins 50% of his bet
        in the last case the player loose his bet
    The game is over when his pot is empty (0$)
    Online learning plateform Openclassrooms.com
    Skill check : Loop in Python
    @Author tizianoadv
"""

# *** Import *** 
import os                       #To pause
from random import randrange    #To generate a random number between 2 limits
from math import ceil
from typing import NamedTuple   #To round a decimal number to the level up

# *** main code *** 

# Initialisation
print("\n\tWelcome to the Casino - Russian roulette \n")
print("Starting pot : 50 $\n")
pot = 50
continue_game = True
id_player = -1
bet = -1 

# Main loop
while( continue_game ):

    #Select a number between 0 - 49 
    while id_player < 0 or id_player >= 50 :
        id_player = input("\nNuméro choisi : ")
        try :
            id_player = int(id_player)
        except ValueError :
            print("It's not a number\n")
            id_player = -1
            continue #To go over the next condition and start at the beginning of the loop
        if id_player < 0 or id_player >= 50 :
            print("It's between 0 - 49 included\n")

    #Select a bet
    while bet <= 0 or bet > pot :
        bet = input("The bet : ")
        try :
            bet = int(bet)
        except ValueError :
            print("It's not a number\n")
            bet = -1
            continue
        if bet <= 0 or bet > pot :
            print("Incorrect bet\n")
    
    # Update of the pot before the game starts
    pot -= bet

    #Generate the winning number (On which the ball falls)
    print("The dearler turns the wheel...")
    win_num = randrange(0, 50)
    print("Winning number : ", win_num)

    #Checking benefits
    benefit = 0
    if win_num == id_player :
        # If the 2 numbers are the same -> benefit = 3 x bet
        benefit = (3 * bet)
        print("The 2 numbers are equal, benefit = ", benefit, "\n")
        pot += benefit + bet
    elif (win_num % 2 == 0) and (id_player % 2 == 0) :
        # If the 2 numbers are even -> benefit : 1/2 x bet
        benefit = ceil(0.5 * bet)
        print("The 2 numbers are even, benefit = ", benefit, "\n")
        pot += benefit + bet
    elif (win_num % 2 != 0) and (id_player % 2 != 0) :
        # If the two numbers are odd -> benefit : 1/2 x bet
        benefit = ceil(0.5 * bet)
        print("The 2 numbers are odd, benefit = ", benefit, "\n")
        pot += benefit + bet
    else :
        # No benefit
        print("Lost ! \n")

    # Updating the pot
    print("Current pot : ", pot, "$\n")

    if pot == 0 :
        # Stop the game
        print("The game is over! \n")        
        continue_game = False
        
#Pause of the system       
os.system("pause")
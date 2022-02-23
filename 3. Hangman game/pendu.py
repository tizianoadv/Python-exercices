"""This file contains the main code of the pendu's game"""

from fonctions import create_hidden_word, user_interface, brain

print("\nWelcome in the hangman game !! \n")

game = [True, 8, ' '] #authorised access & attempts & letter
words =  create_hidden_word() #Word & hidden word

while game[1] > 0:
    #Loop until attempts > 0

    
    game = user_interface(game)#Ask the letter from the user => Return access & attempts
    print("before game1 {}".format(game[1]))
    new_attempt, new_hidden_word = brain(game[1], game[2],words)
    
    #Update new hidden word
    del words[1]
    words.append(new_hidden_word)

    #Update attempt & letter 
    old_attempt = game[1]
    old_letter = game[2]
    game.remove(old_attempt)
    game.append(new_attempt)
    game.remove(old_letter)
    game.append(' ')

    print("end game1 {}".format(game[1]))

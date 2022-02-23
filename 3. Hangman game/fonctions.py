"""This file contains all functions dedicated to the pendu's game"""
from random import randrange
from donnees import word_list
from donnees import attempts

def create_hidden_word():
    """ This function just select a word from the list defined in the file donnees.py
    @return list [str:word seleted, str: word selected or stars (*=letter not find or the letter found)]  """

    hidden_word = list() #Creating an empty list
    word_number = randrange(0,7) #Choosing randomly a number between 0-7

    hidden_word.append(word_list[word_number]) #Adding the word selected to the list
    hidden_word.append(str()) #Adding an empty string
    stars_number = len(hidden_word[0]) #Getting the lenght of the hidden word

    #Creating the hidden word
    for i in hidden_word[0]: 
        tmp1 = str(hidden_word[1])
        tmp2 = tmp1 + "*"
        del hidden_word[1]
        hidden_word.append(tmp2)

    return hidden_word

"""def get_hidden_word():
    hidden_word = list()
    tmp1, tmp2 = create_hidden_word()
    hidden_word.append(tmp1)
    hidden_word.append(tmp2)
    print("hidden_word[0] = {}\nhidden_word[1] = {} ".format(hidden_word[0], hidden_word[1]))
"""

def user_interface(*old_game_params):
    new_game_params = old_game_params[0]
    letter = input("Write a letter : ")
    print("New game params {} \n".format(new_game_params))
    del new_game_params[2]
    new_game_params.append(letter)
    #try: 
    #    lowCletter = str(letter).lower()
    #    if ord(lowCletter) < 97 or ord(lowCletter) > 122:
    #        access.append(0)
    #        raise ValueError("Raise ! Variable is not a lowercase letter")
    #    else:
    #        access.append(letter)
    #except TypeError:
    #    print("Variable is not a lowercase letter")
    #    access.append(0)
    #else:
    #    access.append(attempts)"""

    
    return new_game_params

def brain(attempts_remaining, letter, *parameters):
    list = parameters[0]
    word = list[0]
    old_hidden_word = list[1]
    new_hidden_word = str()
    i=0
    well_move = False

    print("Start of brain : attp = {} ".format(attempts_remaining))

    if attempts_remaining > 0:
        for elt in word:
            tmp = str()
            if (ord(elt) == ord(letter)):
                tmp = new_hidden_word + letter
                well_move = True
            elif old_hidden_word[i] !=  "*":
                tmp = new_hidden_word + elt
            else:
                tmp = new_hidden_word + "*"
                
            new_hidden_word = tmp
            i+=1
        if well_move != True:
            attempts_remaining-=1


        print("End of brain : attp = {} ".format(attempts_remaining))
        print("Hidden word : {}\n".format(new_hidden_word))
        #print("You have {} attempts\n".format(attempts_remaining))

    else:
        print("No letter found ! ")
        print("You have no attempts yet !\n")
    
    return attempts_remaining, new_hidden_word
    

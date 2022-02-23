""
-   functions.py
-   Code defining all required functions to create a line up of 11 football players
-   functions :
        recruitements : Reads all players' names from a file
            @return a list of those names
        createTeam : Creates players objects with names, position and random grades from 0 to 100
            @return a list composed of those objects
        teamPresentation : Prints the list of football player with their grade (fancy way)
        createLineUp : Creates a line up of 11 football players through their grade
            @return a list of those 11 football players name
        lineUpPresentation : Prints the list of the 11 selected football players (fancy way)
-   @author tnardoneadv - Github : https://github.com/tnardoneadv
"""
import os
import random
from player import *

def recruitment():
    """
        recruitements : Reads all players' names from a file
            @return a list of those names
    """
    freeplayers = []
    file = open("list.txt","r")
    for line in file:
        newLine = line[:(len(line)-1)]
        freeplayers.append(newLine)

    file.close
    return freeplayers

def createTeam(listPlayer):
    """
        createTeam : Creates players objects with names, position and random grades from 0 to 100
            @return a list composed of those objects
    """
    team = list()

    i=0
    while i < 20 :

        if i < 5:
            position = "goalkeeper"
        elif (i >= 5) and(i < 10):
            position = "defenders"
        elif (i >= 10) and(i < 15):
            position = "midfielders"
        else:
            position = "strikers"

        team.append(Player(listPlayer[i],position,random.randint(0,100)))
        i=i+1

    return team

def teamPresentation(team):
    """
        teamPresentation : Prints the list of football player with their grade (fancy way)
    """
    print("\n\t\t\t\t\t\t*** Team presentation with players valuation ***\n")
    print("   Goalkeepers : \t\t     Defenders : \t\t    Midfielders : \t\t    Strikers : \n")
    i=0
    j=0
    while i < 5:

        while j < 20:
            print(Player.squadList(team[j]),end=' ')
            j=j+5
        i=i+1
        j=i
        print("\n")


def createLineUp(team):
    """
        createLineUp : Creates a line up of 11 football players through their grade
            @return a list of those 11 football players name
    """
    # *** Line up : 4-4-2 ***
    lineUp = list()
    playerAlreadySelected = list()

    i=0
    j=0
    k=0
    l=0
    maxSelectedPlayers = 11
    maxPlayersInList = 5

    endGoalkeepersList = 1
    endDefendersList = 5
    endMidfieldersList = 9


    while i < maxSelectedPlayers:
        # Selects the 11 best players

        if i < endGoalkeepersList:
            maxPlayersToBeSelected = 1
            startPostionList = 0
        elif (i >= endGoalkeepersList) and (i < endDefendersList):
            maxPlayersToBeSelected = 4
            startPostionList = 5
        elif (i >= endDefendersList) and (i < endMidfieldersList):
            maxPlayersToBeSelected = 4
            startPostionList = 10
        else:
            maxPlayersToBeSelected = 2
            startPostionList = 15

        j=0
        while j < maxPlayersToBeSelected:
            # Selects n best players, depending on the postion
            # Goalkeeper  : 1 player selected
            # Defenders   : 4 players selected
            # Midfielders : 4 players selected
            # Strikers    : 2 players selected

            l = startPostionList
            k = 0
            bestGrade=0
            while k < maxPlayersInList:
                # Select the player with the best player
                # With the best grade
                # If is not already selected or in line up

                if (team[l].grade > bestGrade) and (not (team[l].lastname in playerAlreadySelected)) and (not (team[l].lastname in lineUp)):
                    bestGrade = team[l].grade
                    playerSelected = team[l].lastname
                    playerAlreadySelected.append(playerSelected)
                l+=1
                k+=1
            lineUp.append(playerAlreadySelected[-1])
            del playerAlreadySelected[:]
            j+=1
        i+=j
    return lineUp

def lineUpPresentation(lineUp):
    """
        lineUpPresentation : Prints the list of the 11 selected football players (fancy way)
    """
    print("\n\t\t\t\t\t*** Line up : 4-4-2 ***\n")
    #Strikers
    print("\t\t\t\t{}".format(lineUp[10]),end='')
    print("\t\t\t{}".format(lineUp[9]))
    print("\t\t\t\t  .\t\t\t  .\n")
    #Midfielders
    print("\t{}\t                ".format(lineUp[8]),end='')
    print("{}\t                ".format(lineUp[7]),end='')
    print("{}\t                ".format(lineUp[6]),end='')
    print("{}".format(lineUp[5]))
    print("\t  .\t\t\t  .\t\t\t  .\t\t\t  .\n")
    #Defenders
    print("\t{}\t                ".format(lineUp[4]),end='')
    print("{}\t                ".format(lineUp[3]),end='')
    print("{}\t                ".format(lineUp[2]),end='')
    print("{}".format(lineUp[1]))
    print("\t  .\t\t\t  .\t\t\t  .\t\t\t  .\n")
    #Goalkeeper
    print("\t\t\t\t\t    {}".format(lineUp[0]))
    print("\t\t\t\t\t       .\n")
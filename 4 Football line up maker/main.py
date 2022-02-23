#!env/bin/python3
"""
-   main.py
-   main source code creating a line up of 11 football players
-   @author tnardoneadv - Github : https://github.com/tnardoneadv
"""
from functions import *

#Recruit 20 football players
listPlayer = recruitment()

#Create a team and valuate them
team = createTeam(listPlayer)

#Print the list of football player with their grade
teamPresentation(team)

#Select the best players though their grade and position
#and make a line up
lineUp = createLineUp(team)

#Print the line up
lineUpPresentation(lineUp)
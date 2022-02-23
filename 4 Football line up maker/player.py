"""
-   player.py
-   class Player with constructor and method
-   @author tnardoneadv - Github : https://github.com/tnardoneadv
"""
class Player:
    """Class defining a football with these following features:
    -   his lastname
    -   his position on the pitch
    -   his grade between 0 to 100 chosen randomly"""

    def __init__(self, lastname, position, grade):
        self.lastname = lastname
        self.position = position
        self.grade = grade

    def squadList(self):
        return '{}    \t{}         \t'.format(self.lastname, self.grade)
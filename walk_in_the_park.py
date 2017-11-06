#
# walk_in_the_park.py
#
# implementation of the WalkInThePark behaviour class
#

from behavior import *
import random

class WalkInThePark(Behavior):
    """
    base behavior
    """

    def __init__(self, bbcon = None, sensobs = []):
        super().__init__(bbcon, sensobs)

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def sense_and_act(self):
        moves = [('L', 20), ("TR", 90), ("TL", 50)]
        R = random.choice(moves)
        self.motor_recommendations = R 

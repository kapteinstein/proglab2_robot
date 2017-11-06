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
        moves = [('L', 50), ("R", 50), ("TL", 50), ('TR', 50), ("F", 20), ("B", 20)]
        for i in range(len(moves)):
            self.motor_recommendations = moves[i]


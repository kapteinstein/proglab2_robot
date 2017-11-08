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

    def __init__(self, bbcon=None, sensobs=[], priority=0.2):
        super().__init__(bbcon, sensobs)
        self.match_degree = 0.5

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def sense_and_act(self):
        moves = [('L', 25), ("R", 25), ("TL", 50), ('TR', 50), ("F", 20), ("B",
                                                                           20)]
        self.motor_recommendations = [random.choice(moves)]

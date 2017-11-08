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
        moves = [("TL", 30)* 2, ('TR', 30)* 2, ("TL", 60), ('TR', 60),
        ("F", 20)* 3, ("B", 10)* 3, ("F", 40)* 3, ("B", 20)* 3]
        self.motor_recommendations = [random.choice(moves)]

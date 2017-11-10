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
        super().__init__(bbcon, sensobs, priority=priority)
        self.match_degree = 0.5
        self.name = "walk in the park"

    def consider_deactivation(self):
        # Always active, base behavior
        pass

    def consider_activation(self):
        # Always active, base behavior
        pass

    # Chooses move based on the weights in moves_weight
    def sense_and_act(self):
        moves = [("TL", 30), ('TR', 30), ("L", 60), ('R', 60),
                 ("F", 20), ("B", 10), ("F", 40), ("B", 20)]
        moves_weight = [10,10,10,10,25,10,20,5]
        c_weight = []
        total_weight = 0
        for w in moves_weight:
            c_weight.append(total_weight + w)
            total_weight += w

        R = round(random.random() * total_weight, 3)

        for i in range(len(moves_weight)):
            if R < c_weight[i]:
                self.motor_recommendations = [moves[i]]
                break

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
        moves = [("TL", 30), ('TR', 30), ("TL", 60), ('TR', 60),
                 ("F", 20), ("B", 10), ("F", 40), ("B", 20)]
        moves_weight = [15,15,5,5,25,20,10,5]
        total_weight = 100
        R = round(random.random() * total_weight, 3)

        for i in range(len(moves_weight)):
            if R < moves_weight[i]:
                self.motor_recommendations = [moves[i]]
                break

#
# walk_in_the_park.py
#
# implementation of the WalkInThePark behaviour class
#

from behavior import *

class WalkInThePark(Behavior):
    """
    base behavior
    """

    def __init__(self, bbcon = None, sensobs = []):
        super(self.__init__(bbcon, sensob))

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def sense_and_act(self):
        self.motor_recommendations = [('L', 20)]

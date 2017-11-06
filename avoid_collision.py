#
# avoid_collision.py
#
# implementation of the AvoidCollision behaviour class
#

from behavior import *


class AvoidCollision(Behavior):
    """
    turn around 180 deg if an object is close
    """

    def __init__(self, bbcon=None, sensobs=[]):
        self.motor_recommendations = []
        super().__init__(bbcon, sensobs=sensobs)

    def consider_deactivation(self):
        # deactivate behavior if object is farther away than 10cm
        if self.sensobs[0].value > 10:
            self.active_flag = False

    def consider_activation(self):
        # activate behavior if object is closer than 10cm
        if self.sensobs[0].value < 10:
            self.active_flag = True

    def sense_and_act(self):
        # higher match degree if object is closer
        self.match_degree = abs(10 - self.sensobs[0].value) / 10
        self.motor_recommendations = [('TR', 180)]

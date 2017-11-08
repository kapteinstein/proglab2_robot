#
# avoid_collision.py
#
# implementation of the AvoidCollision behaviour class
#

from behavior import *
import random

class AvoidCollision(Behavior):
    """
    turn around 180 deg if an object is close
    """

    def __init__(self, bbcon=None, sensobs=[], priority = 0.8):
        super().__init__(bbcon, sensobs=sensobs, priority=priority)
        self.trigger_dist = 20
        self.motor_recommendations = []

    def consider_deactivation(self):
        # deactivate behavior if object is farther away than 10cm
        if self.sensobs[0].value > self.trigger_dist:
            self.active_flag = False
            self.match_degree = 0
            self.motor_recommendations = []

    def consider_activation(self):
        # activate behavior if object is closer than 10cm
        if self.sensobs[0].value < self.trigger_dist:
            self.active_flag = True

    def sense_and_act(self):
        # higher match degree if object is closer
        self.match_degree = max((self.trigger_dist - self.sensobs[0].value),
                0)/self.trigger_dist
        direction = random.choice(['TR', 'TL'])
        self.motor_recommendations = [(direction, 180)]

from behavior import *
import random


class DetectRed(Behavior):
    """
    go back if red is detected
    """

    def __init__(self, bbcon=None, sensobs=[], priority=0.6):
        super().__init__(bbcon, sensobs=sensobs, priority=priority)
        self.trigger_dist = 30
        self.motor_recommendations = []
        self.name = "detect red"

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

        percent_red = self.sensobs[1].value or 0

        self.match_degree = percent_red

        self.motor_recommendations = [("B", 100)]

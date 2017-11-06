#
# halt.py
#
# implementation of the halt behaviour class
#

from behavior import *
from zumo_button import ZumoButton


class HaltBehavior(Behavior):
    """
    Halting behavior
    """

    def __init__(self, bbcon=None, sensobs=[]):
        self.zumo_button = ZumoButton()
        self.motor_recommendations = []
        super().__init__(bbcon, sensobs)
        self.halt_request = True

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def sense_and_act(self):
        self.match_degree = 1 if self.zumo_button.button_pressed() else 0

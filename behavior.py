#
# behavior.py
#
# implementation of the behaviour class and its subclasses
#

class Behavior(object):
    """
    modular unit designed to analyze a subset of the sensory information as
    the basis for determining a motor request
    """

    def __init__(self, bbcon = None, sensobs = [], active_flag = True):
        self.bbcon = bbcon
        self.sensob = sensob
        self.motor_recommendations = []
        self.active_flag = active_flag
        self.halt_request = False
        self.priority = priority
        self.match_degree = 0
        self.weight = 0

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def update(self):
        # TODO: change this when we know what is going on with reactivation

        # consider changing active_flag
        if self.active_flag:
            self.consider_deactivation()
            self.sense_and_act()
            self.weight = self.priority * self.match_degree
        else:
            self.consider_activation()

    def sense_and_act(self):
        pass
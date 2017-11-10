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

    def __init__(self, bbcon = None, sensobs = [], active_flag = True, priority=1):
        self.bbcon = bbcon
        self.sensobs = sensobs
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
        # consider changing active_flag
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.sense_and_act()

        self.weight = self.priority * self.match_degree

    def sense_and_act(self):
        pass

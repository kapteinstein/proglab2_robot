import random

class Arbitrator():

    def __init__(self, bbcon):
        self.bbcon = bbcon
        
    def choose_action(self, stochastic):
        if stochastic:
            return self.choose_action_stochastic(self)
        else:
            return self.choose_action_deterministic(self)

    # Chooses the behavior with the highest weight
    def choose_action_deterministic(self):
        highest_weight = 0
        winning_behavior = None
        active_behaviors = self.bbcon.active_behaviors
        for behavior in active_behaviors:
            if behavior.weight > highest_weight:
                highest_weight = behavior.weight
                winning_behavior = behavior
        return (winning_behavior.motor_recommandations, winning_behavior.halt_request)
            

    # Chooses the behavior stochasticitly
    def choose_action_stochastic(self):
        active_behaviors = self.bbcon.active_behaviors
        behavior_weights = []
        total_weight = 0
        for behavior in active_behaviors:
            behavior_weights.append(total_weight + behavior.weight)
            total_weight += behavior.weight
        R = random() * total_weight

        # Choose behavior
        for i in range(len(behavior_weights)):
            if R < behavior_weights[i]:
                return (active_behaviors[i].motor_recommandations, active_behaviors[i].halt_request)
        
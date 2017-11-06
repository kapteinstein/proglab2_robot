import random


class Arbitrator():
    def __init__(self):
        pass

    def choose_action(self, active_behaviors, stochastic=False):
        if stochastic:
            return self.choose_action_stochastic(active_behaviors)
        else:
            return self.choose_action_deterministic(active_behaviors)

    # Chooses the behavior with the highest weight
    def choose_action_deterministic(self, active_behaviors):
        highest_weight = 0
        best_behavior = None
        for behavior in active_behaviors:
            if behavior.weight >= highest_weight:
                highest_weight = behavior.weight
                best_behavior = behavior
        return (best_behavior.motor_recommandations,
                best_behavior.halt_request)

    # Chooses the behavior stochasticitly
    def choose_action_stochastic(self, active_behaviors):
        behavior_weights = []
        total_weight = 0
        for behavior in active_behaviors:
            behavior_weights.append(total_weight + behavior.weight)
            total_weight += behavior.weight

        R = round(random() * total_weight, 4)

        # Choose behavior
        for i in range(len(behavior_weights)):
            if R < behavior_weights[i]:
                return (active_behaviors[i].motor_recommandations,
                        active_behaviors[i].halt_request)

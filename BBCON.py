import sys


class BBCON():
    def __init__(
            self,
            arbitrator,
            motobs,
            sensobs,
            behaviors=[],
            active_behaviors=[],
    ):
        self.arbitrator = arbitrator
        self.behaviors = behaviors
        for active_behavior in active_behaviors:
            if active_behavior not in behaviors:
                raise Exception("Active behavior must be in behaviors")
            active_behavior.consider_activate()
        self.active_behaviors = active_behaviors
        self.sensobs = sensobs
        self.motobs = motobs

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def activate_behavior(self, behavior):
        if behavior not in self.behaviors:
            raise Exception("Behavior must be in behaviors to be activated")
        self.active_behaviors.append(behavior)
        behavior.consider_activation()

    def deactivate_behavior(self, behavior):
        """
        Deactivates a behavior, and returns a boolean value
        true if the behavior was active, and false if it was not
        """
        exits = behavior in self.active_behaviors
        if exists:
            self.active_behaviors.remove(behavior)
            active_behavior.consider_deactivation()

        return exists

    def update_all_sensobs(self):
        """ Updates all sensobs """
        for sensob in self.sensobs:
            sensob.update()

    def update_all_behaviors(self):
        """ Updates all active behaviors """
        for behavior in self.active_behaviors:
            behavior.update()

    def get_result_action(self):
        """
        Returns a tuple with motor recommendations for each motor, and a
        boolean telling the program to halt
        """
        motor_re, halt = self.arbitrator.choose_action(self.active_behaviors)
        return motor_re, halt

    def update_motobs(self, recommendations):
        for recommendation, motob in zip(recommendations, self.motobs):
            motob.update(recommendation)

    def run_one_timestep(self):

        self.update_all_sensobs()  # Is this done in the behaviors?
        self.update_all_behaviors()

        # or does the arbitrator have the required fields?
        result, halt = self.get_result_action()

        # enable some verbose logging
        if len(sys.argv) > 1 and sys.argv[1] == '-v':
            print("behaviors: ")
            for behavior in self.active_behaviors:
                print("{0: <16}: ".format(bahavior.name), end='')
                print("weight: {:.4f},\tmotor_rec:{}".format(behavior.weight,
                    behavior.motor_recommendations))
            print("--> action: {}".format(result))

        if halt:
            print("Got HALT request... Halting now")
            self.motobs[0].stop()
            sys.exit(0)

        self.update_motobs(result)

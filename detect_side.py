from behavior import *



class DetectSide(Behavior):

    def __init__(self, bbcon = None, sensobs = [], priority = 0.8):
        super().__init__(bbcon, sensobs = sensobs, priority = priority)
        self.act_counter = 0
        self.deact_counter = 0
        self.match_degree_counter = 0
        self.name = "detect side"


    # Behavior active for 2 cycles
    def consider_deactivation(self):
        if self.deact_counter == 2:
            self.active_flag = False
            self.match_degree = 0
            self.motor_recommendations = []
            self.deact_counter = 0
            self.match_degree_counter = 0
        else:
            self.deact_counter +=1

    # Behavior deactivated for 3 cycles
    def consider_activation(self):
        if self.act_counter == 3:
            self.active_flag = True
            self.active_counter = 0
        else:
            self.act_counter += 1
    
    # Runs when active
    def sense_and_act(self):
        sensor_tuple = self.sensobs[0].update()

        # Check if object to the left
        if sensor_tuple[0] == True and sensor_tuple[1] == False:
            self.match_degree_counter += 1
            self.match_degree = self.match_degree_counter * 0.41
            self.motor_recommendations = [("R", 40)]
        
        # Check if object to the right
        if sensor_tuple[0] == False and sensor_tuple[1] == True:
            self.match_degree_counter += 1
            self.match_degree = self.match_degree_counter * 0.41
            self.motor_recommendations = [("L", 40)]
        
        # If obstacle on both sides, drive straight
        if sensor_tuple[0] == True and sensor_tuple[1] == True:
            self.match_degree_counter += 1
            self.match_degree = self.match_degree_counter * 0.41
            self.motor_recommendations = [("F", 40)]
        

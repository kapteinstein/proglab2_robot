import Motors

class Motob:
    def __init__(self, bbcon):
        self.motors = Motors()
        self.value = None
        self.bbcon = bbcon

    def update(self, motorRec):
        self.value = motorRec
        self.operationalize()

    def operationalize(self):
        for rec in self.value:
            if rec[0] == "F":
                self.motors.forward(speed=rec[1]*0.01)
            elif rec[0] == "B":
                self.motors.backward(speed=rec[1]*0.01)
            elif rec[0] == "L":
                pass
            elif rec[0] == "R":
                pass
            elif rec[0] == "TL":
                self.motors.set_value([[rec[1]],[0]])
            elif rec[0] == "TR":
                self.motors.set_value([[0],[rec[1]]])




    def turnDegrees(deg):
        return 0.0028 * deg #Så mye snur den visst


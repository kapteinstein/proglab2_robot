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
                motors.forward(speed=rec[1]*0.01)
            elif rec[0] == "B":
                motors.backward(speed=rec[1]*0.01)


    def turnDegrees(deg):
        return 0.0028 * deg #Så mye snur den visst

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
        m = Motors()
        for rec in self.value:
            if rec[0] == "F":
                m.forward(rec[1]*0.01, 3)
            elif rec[0] == "B":
                m.backward(rec[1]*0.01, 3)
            elif rec[0] == "L":
                m.set_value([[rec[1]*0.01*0.5],[rec[1]*0.01]], 3)
            elif rec[0] == "R":
                m.set_value([[rec[1]*0.01],[rec[1]*0.01*0.5]], 3)
            elif rec[0] == "TL":
                m.set_value([[0],[rec[1]]])
            elif rec[0] == "TR":

            elif rec[0] == "S":
                m.stop()




    def turnDegrees(deg):
        return 0.0028 * deg #Så mye snur den visst

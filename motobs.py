import Motors

class Motob:
    def __init__(self):
        self.motors = Motors()
        self.value = None

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
                m.left(0.5, 5)
            elif rec[0] == "TR":
                m.right(0.5, 5)
            elif rec[0] == "S":
                m.stop()

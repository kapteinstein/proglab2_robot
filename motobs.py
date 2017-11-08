from motors import Motors


class Motob:
    def __init__(self):
        self.motors = Motors()
        self.value = None

    def update(self, motorRec):
        self.value = [motorRec]
        self.operationalize()

    def stop(self):
        self.motors.stop()

    def operationalize(self):
        for rec in self.value:
            if rec[0] == "F":
                self.motors.forward(rec[1] * 0.01, 0.5)
            elif rec[0] == "B":
                self.motors.backward(rec[1] * 0.01, 0.5)
            elif rec[0] == "L":
                self.motors.set_value([rec[1] * 0.01 * 0.0, rec[1] * 0.01],
                                      0.5)
            elif rec[0] == "R":
                self.motors.set_value([rec[1] * 0.01, rec[1] * 0.01 * 0.0],
                                      0.5)
            elif rec[0] == "TL":
                self.motors.left(0.5, rec[1] / 60)
            elif rec[0] == "TR":
                self.motors.right(0.5, rec[1] / 60)
            elif rec[0] == "S":
                self.motors.stop()

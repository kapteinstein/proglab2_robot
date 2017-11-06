# sensob.py
#
# Sensor object, serves as an interface between one or more sensors and the BBCONs behaviors
#
# implementing sensob and its subclasses
from irproximity_sensor import IRProximitySensor
from ultrasonic import Ultrasonic
from reflectance_sensors import ReflectanceSensors
from irproximity_sensor import *


class Sensob(object):
    def __init__(self, sensors=[]):
        self.sensors = sensors
        self.value = None

    def update(self):
        sensor_data = []
        for sensor in self.sensors:
            sensor_data.append(sensor.update())
        self.process_sensor_data(sensor_data)
        return self.value

    # Process the sensor_data and set self.value depending on what kind of sensob
    def process_sensor_data(self, sensor_data=[]):
        pass


class Proximity(Sensob):
    """
    check if there is another object within 5cm in front or of the sides of
    the robot. if that is the case, self.value is set to True
    """

    def __init__(self):
        ir = IRProximitySensor()
        us = Ultrasonic()
        super().__init__([ir, us])

    def process_sensor_data(self, sensor_data):
        ir_data = sensor_data[0]
        us_data = sensor_data[1]

        too_close = False
        for measurement in ir_data:  # check left and right proximity sensor
            if measurement == True:
                too_close = True
        if us_data < 5:  # closer than 5 cm in front
            too_close = True

        self.value = too_close


class EdgeDetector(Sensob):
    def __init__(self):
        rs = ReflectanceSensors()
        super().__init__(rs)

    def process_sensor_data(self, sensor_data):
        for value in sensor_data:
            if value == 0:
                self.value = 0


class MeasureDistance(Sensob):
    """
    return distance to object in front of the robot
    """

    def __init__(self):
        self.us = Ultrasonic()
        super().__init__(sensors=[self.us])

    def process_sensor_data(self, sensor_data):
        self.value = sensor_data[0]
        
class IRSensob(Sensob):


    def __init__(self):
        super(IRSensob, self).__init__()
        self.sensors.append(IRProximitySensor())

    def update(self):
        return


class IRSensobLeft(IRSensob):

    def __init__(self):
        super(IRSensobLeft, self).__init__()
        self.value = False

    def update(self):
        self.value = self.sensors[0].update()[0]
        return self.value

    def get_value(self):
        return self.value


class IRSensobRight(IRSensob):

    def __init__(self):
        super(IRSensobRight, self).__init__()
        self.value = False

    def update(self):
        self.value = self.sensors[0].update()[1]
        return self.value

    def get_value(self):
        return self.value


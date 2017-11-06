# sensob.py
# 
# Sensor object, serves as an interface between one or more sensors and the BBCONs behaviors
#
# implementing sensob and its subclasses
from irproximity_sensor import IRProximitySensor 
from ultrasonic import Ultrasonic
from reflectance_sensors import ReflectanceSensors


class Sensob(object):

    def __init__(self, sensors = []):
        self.sensors = sensors
        self.value = None


    def update(self):
        sensor_data = []
        for sensor in self.sensors:
            sensor_data.append(sensor.update())
        self.process_sensor_data(sensor_data)
        return self.value

    # Process the sensor_data and set self.value depending on what kind of sensob
    def process_sensor_data(self, sensor_data = []):
        pass


class Proximity(Sensob):

    def __init__(self):
        ir = IRProximitySensor()
        us = Ultrasonic()
        super().__init__([ir, us])
    
    def process_sensor_data(self, sensor_data):
        pass

class EdgeDetector(Sensob):

    def __init__(self):
        rs = ReflectanceSensors()
        super().__init__(rs)

    def process_sensor_data(self, sensor_data):
        for value in sensor_data:
            if value == 0:
                self.value = 0
            
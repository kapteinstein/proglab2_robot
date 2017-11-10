# sensob.py
#
# Sensor object, serves as an interface between one or more sensors and the BBCONs behaviors
#
# implementing sensob and its subclasses
from irproximity_sensor import IRProximitySensor
from ultrasonic import Ultrasonic
from reflectance_sensors import ReflectanceSensors
from irproximity_sensor import *
from camera import *
from imager2 import Imager
from PIL import Image
import operator


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
        ir = IRProximitySensor()
        super(IRSensob, self).__init__(sensors=[ir])

    def process_sensor_data(self, sensor_data):
        self.value = sensor_data[0]


class Camob(Sensob):
    def __init__(self):
        self.image_width = 128
        self.image_height = 96
        self.size = self.image_height * self.image_width

        cam = Camera(self.image_width, self.image_height, img_rot=0)

        # This defines "what" is counted as red
        self.upper = (256, 40, 40)
        self.lower = (50, 0, 0)

        super().__init__([cam])

    def process_sensor_data(self, sensor_data):
        img = sensor_data[0]
        image = Imager(image=img)

        image = image.map_color_wta()

        count_red = 0

        for pixel in image.image.getdata():
            if pixel == (255, 0, 0):
                count_red += 1

        print("Count of red pixels: ", count_red)

        self.value = count_red / self.size

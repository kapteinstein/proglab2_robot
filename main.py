import time

from robodemo import *
from BBCON import BBCON
from Arbitrator import Arbitrator
from motobs import Motob
from zumo_button import ZumoButton
from sensob import *

from walk_in_the_park import WalkInThePark
from halt_behavior import HaltBehavior
from avoid_collision import AvoidCollision
from detect_side import DetectSide


def main():
    print("Waiting for press")
    ZumoButton().wait_for_press()
    print("Button pressed...")
    arbitrator = Arbitrator()
    motob = Motob()
    distance_sensor = MeasureDistance()
    distance_sensor.update()  # Force update
    ir_sensor = IRSensob()

    bbcon = BBCON(arbitrator, [motob], [distance_sensor, ir_sensor])

    sideDetect = DetectSide(bbcon = bbcon, sensobs = [ir_sensor])
    parkWalk = WalkInThePark(bbcon=bbcon)
    halting = HaltBehavior(bbcon=bbcon)
    # collision = AvoidCollision(bbcon=bbcon, sensobs=[distance_sensor])

    bbcon.add_behavior(parkWalk)
    bbcon.activate_behavior(parkWalk)

    bbcon.add_behavior(halting)
    bbcon.activate_behavior(halting)

    bbcon.add_behavior(sideDetect)
    bbcon.activate_behavior(sideDetect)

    time.sleep(0.1)

    while True:
        bbcon.run_one_timestep()


def demo():
    tourist()


if __name__ == '__main__':
    main()

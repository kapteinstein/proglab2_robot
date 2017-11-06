import time

from robodemo import *
from BBCON import BBCON
from Arbitrator import Arbitrator
from motobs import Motob
from zumo_button import ZumoButton

from walk_in_the_park import WalkInThePark
from halt_behavior import HaltBehavior
from avoid_collision import AvoidCollision


def main():
    print("Waiting for press")
    ZumoButton().wait_for_press()
    print("Button pressed...")
    arbitrator = Arbitrator()
    motob = Motob()
    bbcon = BBCON(arbitrator, [motob], [])

    parkWalk = WalkInThePark(bbcon=bbcon)
    halting = HaltBehavior(bbcon=bbcon)
    collision = AvoidCollision(bbcon=bbcon)

    bbcon.add_behavior(parkWalk)
    bbcon.activate_behavior(parkWalk)

    bbcon.add_behavior(halting)
    bbcon.activate_behavior(halting)

    bbcon.add_behavior(collision)
    bbcon.activate_behavior(collision)

    time.sleep(0.1)

    while True:
        bbcon.run_one_timestep()


def demo():
    tourist()


if __name__ == '__main__':
    main()

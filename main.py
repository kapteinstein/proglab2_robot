from robodemo import *
from BBCON import BBCON
from Arbitrator import Arbitrator
from motobs import Motob

from walk_in_the_park import WalkInThePark


def main():

    arbitrator = Arbitrator()
    motob = Motob()
    bbcon = BBCON(arbitrator, [motob], [])

    parkWalk = WalkInThePark(bbcon=bbcon)

    bbcon.add_behavior(parkWalk)
    bbcon.activate_behavior(parkWalk)

    while True:
        bbcon.run_one_timestep()


def demo():
    tourist()


if __name__ == '__main__':
    main()

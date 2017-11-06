# Proglab2 - Project 6

> Project 6 in TDT4113: Behavior-Based Robot Control


## Behaviors

- Walk in park (random search)
- Crash detector
    - Ultrasonic sensor
    - IR proximity sensor
- Red flag detector
    - Camera
    - Only use camera when distance is less than XX


## Install

To install the system, run the following commands
```bash
$ git clone https://github.com/kapteinstein/proglab2_robot
$ sudo ln -s /home/$USER/proglab2_robot/plab-robot.service /etc/systemd/system/plab-robot.service
$ sudo systemct enable plab-robot # disable to disable autostart
```

The robot will now fetch a new version every time it is booted with a connected ethernet cable. The `main.py` is also executed automatically.

To see the status of the execution (after latest boot), run:

```bash
$ sudo journalctl -u plab-robot -b
```

To stop and start the execution run
```bash
$ sudo systemctl stop plab-robot # You can now run other test stuff
$ sudo systemctl start plab-robot

```

## About

Anders Granås, Erik Liodden, Odin Ugedal, Ole Kristian Vingdal

import finch
import time

#connect to the Finch robot
robot = finch.Finch()

#green light, move forward
robot.led(0, 255, 0)
robot.wheels(0.75, 0.75)
time.sleep(1.5)

#turn off lights and wheels
robot.halt()

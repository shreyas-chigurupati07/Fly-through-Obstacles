from djitellopy import Tello
import time

tello = Tello()
tello.connect()
tello.turn_motor_on()
time.sleep(10)
tello.turn_motor_off()
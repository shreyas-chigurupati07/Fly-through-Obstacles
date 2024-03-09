from djitellopy import Tello
import time
import csv

# Filepath to your CSV
csv_filepath = 'pathnew.csv'

# Lists to hold the coordinates
x_coords = []
y_coords = []
z_coords = []

# Open and read the CSV
with open(csv_filepath, mode='r', newline='') as file:
    reader = csv.reader(file)
    
    # Read x coordinates
    x_coords = [int(i) for i in next(reader)]
    
    # Read y coordinates
    y_coords = [int(i) for i in next(reader)]
    
    # Read z coordinates
    z_coords = [int(i) for i in next(reader)]

    # Skip the next six rows which you don't want
    for _ in range(6):
        next(reader)

# Print out the lists (for testing)
print("X Coordinates:", x_coords)
print("Y Coordinates:", y_coords)
print("Z Coordinates:", z_coords)

tello = Tello()
tello.connect()
tello.takeoff()
# tello.turn_motor_on()
# x = 50
# tello.move_up(x)
# time.sleep(10)
height = tello.get_height()
print("Height: ", height)
x, y, z = 50, 50, 50
speed = 15
tello.go_xyz_speed(x, y, z, speed)
x, y, z = -50, -50, -50
speed = 15
tello.go_xyz_speed(x, y, z, speed)
# time.sleep(10)
tello.land()
flight_time = tello.get_flight_time()
power = tello.get_battery()
print("Power= ", power)
print("Flight Time: ", flight_time)

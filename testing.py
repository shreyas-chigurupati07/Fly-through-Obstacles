from djitellopy import Tello
import time
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
# Filepath to your CSV
csv_filepath = 'trajnew25newbloat.csv'

# Lists to hold the coordinates
x_coords = []
y_coords = []
z_coords = []
yaw = []
vx = []
vy = []
vz = []
yawdot = []


# Open and read the CSV
with open(csv_filepath, mode='r', newline='') as file:
    reader = csv.reader(file)
    # print(reader)
    
    # Read x coordinates
    x_coords = [float(i) for i in next(reader)]
    
    # Read y coordinates
    y_coords = [float(i) for i in next(reader)]
    
    # Read z coordinates
    z_coords = [float(i) for i in next(reader)]
    yaw = [float(i) for i in next(reader)]
    vx_coords = [float(i) for i in next(reader)]
    vy_coords = [float(i) for i in next(reader)]
    vz_coords = [float(i) for i in next(reader)]
    yawdot_coords = [float(i) for i in next(reader)]




# Print out the lists (for testing)

x_coords = [int(x*100) for x in x_coords]
y_coords = [int(y*100) for y in y_coords]
z_coords = [int(z*100) for z in z_coords]
vx_coords = [int(vx*100) for vx in vx_coords]
vy_coords = [int(vy*100) for vy in vy_coords]
vz_coords = [int(vz*100) for vz in vz_coords]
yawdot_coords = [int(yawdot) for yawdot in yawdot_coords]
# y_coords = [int(y*100) for y in y_coords]
# z_coords = [int(z*100) for z in z_coords]

print(len(vx_coords))
# rel_x = []
# rel_y = []
# rel_z = []
# rel_x.append(x_coords[0])
# rel_y.append(y_coords[0])
# rel_z.append(z_coords[0])
# for i in range(len(x_coords)-1):
#     rel_x.append(x_coords[i+1]-x_coords[i])
#     rel_y.append(y_coords[i+1]-y_coords[i])
#     rel_z.append(z_coords[iPower=  92
# {'mid': -1, 'x': -100, 'y': -100, 'z': -100, 'mpry': '0,0,0', 'pitch': 0, 'roll': 0, 'yaw': 0, 'vgx': 0, 'vgy': 0, 'vgz': 0, 'templ': 43, 'temph': 46, 'tof': 101, 'h': 100, 'bat': 89, 'baro': 221.5, 'time': 10, 'agx': 1.0, 'agy': -8.0, 'agz': -981.0}
# {'mid': -1, 'x': -100, 'y': -100, 'z': -100, 'mpry': '0,0,0', 'pitch': 1, 'roll': 2, 'yaw': 0, 'vgx': 0, 'vgy': 0, 'vgz': 0, 'templ': 44, 'temph': 47, 'tof': 104, 'h': 100, 'bat': 87, 'baro': 221.49, 'time': 13, 'agx': 5.0, 'agy': 1.0, 'agz': -1001.0}
# {'mid': -1, 'x': -100, 'y': -100, 'z': -100, 'mpry': '0,0,0', 'pitch': 1, 'roll': 4, 'yaw': 0, 'vgx': 0, 'vgy': 1, 'vgz': 0, 'templ': 45, 'temph': 48, 'tof': 111, 'h': 110, 'bat': 86, 'baro': 221.62, 'time': 16, 'agx': 3.0, 'agy': 5.0, 'agz': -1004.0}
# {'mid': -1, 'x': -100, 'y': -100, 'z': -100, 'mpry': '0,0,0', 'pitch': 0, 'roll': 3, 'yaw': 0, 'vgx': 0, 'vgy': 1, 'vgz': 0, 'templ': 46, 'temph': 49, 'tof': 118, 'h': 110, 'bat': 84, 'baro': 221.77, 'time': 20, 'agx': 0.0, 'agy': 7.0, 'agz': -1002.0}
# {'mid': -1, 'x': -100, 'y': -100, 'z': -100, 'mpry': '0,0,0', 'pitch': 0, 'roll': 5, 'yaw': 0, 'vgx': 0, 'vgy': 1, 'vgz': 0, 'templ': 47, 'temph': 49, 'tof': 108, 'h': 110, 'bat': 83, 'baro': 221.56, 'time': 22, 'agx': -4.0, 'agy': 11.0, 'agz': -1011.0}
# {'mid': -1, 'x': -100, 'y': -100, 'z': -100, 'mpry': '0,0,0', 'pitch': -3, 'roll': 1, 'yaw': 0, 'vgx': 0, 'vgy': 0, 'vgz': 0, 'templ': 47, 'temph': 50, 'tof': 95, 'h': 90, 'bat': 81, 'baro': 221.43, 'time': 26, 'agx': 9.0, 'agy': 0.0, 'agz': -995.0}
# {'mid': -1, 'x': -100, 'y': -100, 'z': -100, 'mpry': '0,0,0', 'pitch': -2, 'roll': 1, 'yaw': 0, 'vgx': 0, 'vgy': 0, 'vgz': 0, 'templ': 48, 'temph': 50, 'tof': 77, 'h': 70, 'bat': 79, 'baro': 221.23, 'time': 30, 'agx': 11.0, 'agy': -1.0, 'agz': -996.0}
# Flight Time:  34+1]-z_coords[i])

for i in range(len(vx_coords)):
    # print("x, y, z are abs: ", x_coords[i],y_coords[i],z_coords[i])
    print("vx, vy, vz are abs: ", vx_coords[i],vy_coords[i],vz_coords[i])
    print("yawdot are abs: ", yawdot_coords[i])
# for i in range(len(rel_x)):
#     print("x, y, z are: ", rel_x[i],rel_y[i],rel_z[i])
# x = userstates['x']
# y = userstates['y']
# z = userstates['z']
# xdes = userstates['x_des']
# ydes = userstates['y_des']
# zdes = userstates['z_des']
# vx = userstates['vx']
# vy = userstates['vy']
# vz = userstates['vz']
# vxdes = userstates['vx_des']
# vydes = userstates['vy_des']
# vzdes = userstates['vz_des']
fig1 = plt.figure()
ax = plt.axes(projection='3d')
# ax.plot3D(self.MP[0, :], self.MP[1, :],self.MP[2, :], 'green')
ax.plot3D(x_coords, y_coords,z_coords, 'green',label='abs')
ax.plot3D(vx_coords, vy_coords,vz_coords, 'yellow',label='vel')
# ax.plot3D(rel_x,rel_y,rel_z,'red',label='rel')
ax.set_title('3D trajectory visualization')
ax.legend(loc='upper right')
ax.grid(True)
plt.show()
#-------------------
# odometry correction after getting the current drone states
# print("X Coordinates:", x_coords)
# print("Y Coordinates:", y_coords)
# print("Z Coordinates:", z_coords)t
# Try new path with xyz speed after xyz correction
# try xyzcurved on this file
# try changing bloats
# rc model with traj not waypoints
# drone command debugging sample square map print state
try:
    tello = Tello()
    tello.connect()
    power = tello.get_battery()
    print("Power= ", power)
    tello.takeoff()
    speeds = 90
    tello.go_xyz_speed(0,0,22,speeds)
    time.sleep(0.2)
    tello.get_current_state()
    for i in range(len(vx_coords)):
        tello.send_rc_control(-vy_coords[i],vx_coords[i],vz_coords[i],yawdot_coords[i])
        # time.sleep(0.029)
        time.sleep(0.034)
        tello.get_current_state()    
    tello.land()
    flight_time = tello.get_flight_time()
    print("Flight Time:",flight_time)
except KeyboardInterrupt:
    # HANDLE KEYBOARD INTERRUPT AND STOP THE DRONE COMMANDS
    print('keyboard interrupt')
    tello.emergency()
    tello.emergency()
    tello.end()
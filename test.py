from djitellopy import Tello
import time
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import threading

def running_sim():
        
    
    # Filepath to your CSV
    csv_filepath = 'pathkotha1.csv'

    # Lists to hold the coordinates
    x_coords = []
    y_coords = []
    z_coords = []

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

    # Print out the lists (for testing)

    x_coords = [int(x*100) for x in x_coords]
    y_coords = [int(y*100) for y in y_coords]
    z_coords = [int(z*100) for z in z_coords]
    print(len(x_coords))
    rel_x = []
    rel_y = []
    rel_z = []
    rel_x.append(x_coords[0])
    rel_y.append(y_coords[0])
    rel_z.append(z_coords[0])
    for i in range(len(x_coords)-1):
        rel_x.append(x_coords[i+1]-x_coords[i])
        rel_y.append(y_coords[i+1]-y_coords[i])
        rel_z.append(z_coords[i+1]-z_coords[i])

    for i in range(len(x_coords)):
        print("x, y, z are abs: ", x_coords[i],y_coords[i],z_coords[i])
    for i in range(len(rel_x)):
        print("x, y, z are: ", rel_x[i],rel_y[i],rel_z[i])
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
    ax.plot3D(rel_x,rel_y,rel_z,'red',label='rel')
    ax.set_title('3D trajectory visualization')
    ax.legend(loc='upper right')
    ax.grid(True)
    plt.show()
    #-------------------
    # fig2, axs = plt.subplots(2, 3, figsize=(15, 8))

    # Plot the data in each subplotoords[0])
    # rel_y.append(y_coords[0])
    # rel_z.append(z_coords[0])
    # axs[0, 0].set_ylabel('X (m)')
    # axs[0, 0].set_xlabel('time (s)')
    # axs[0, 0].legend(loc='upper right')
    # axs[0, 0].grid(True)
    # axs[0, 1].plot(t,ydes,label='ydes')
    # axs[0, 1].plot(t,y,label='y')
    # axs[0, 1].set_title('Position Y')
    # axs[0, 1].set_ylabel('Y (m)')
    # axs[0, 1].set_xlabel('time (s)')
    # axs[0, 1].legend(loc='upper right')
    # axs[0, 1].grid(True)
    # axs[0, 2].plot(t,zdes,label='zdes')
    # axs[0, 2].plot(t,z,label='z')
    # axs[0, 2].set_title('Position Z')
    # axs[0, 2].set_ylabel('Z (m)')
    # axs[0, 2].set_xlabel('time (s)')
    # axs[0, 2].legend(loc='upper right')
    # axs[0, 2].grid(True)
    # axs[1, 0].plot(t,vxdes,label='vxdes')
    # axs[1, 0].plot(t,vx,label='vx')
    # axs[1, 0].set_title('Velcoity X')oords[0])
    # rel_y.append(y_coords[0])
    # rel_z.append(z_coords[0])
    # axs[1, 0].set_ylabel('Vx (m/s)')
    # axs[1, 0].set_xlabel('time (s)')
    # axs[1, 0].legend(loc='upper right')
    # axs[1, 0].grid(True)
    # axs[1, 1].plot(t,vydes,label='vydes')
    # axs[1, 1].plot(t,vy,label='vy')
    # axs[1, 1].set_title('Velcoity Y')
    # axs[1, 1].set_ylabel('Vy (m/s)')
    # axs[1, 1].set_xlabel('time (s)')
    # axs[1, 1].legend(loc='upper right')
    # axs[1, 1].grid(True)
    # axs[1, 2].plot(t,vzdes,label='vzdes')
    # axs[1, 2].plot(t,vz,label='vz')
    # axs[1, 2].set_title('Velcoity Z')
    # axs[1, 2].set_ylabel('Vz (m/s)')
    # axs[1, 2].set_xlabel('time (s)')
    # axs[1,2].legend(loc='upper right')
    # axs[1, 2].grid(True)oords[0])
    # rel_y.append(y_coords[0])
    # rel_z.append(z_coords[0])

    # # Adjust layout
    # plt.tight_layout()
    # # Show the plot
    # plt.show()
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
        speeds = 90 #tune
        for i in range(len(rel_x)):
            tello.go_xyz_speed(rel_x[i],rel_y[i],rel_z[i],speeds)
            tello_state = tello.get_current_state()
            print(tello_state)
            time.sleep(0.2) #tune
        # for i in range(len(x_coords)-1):
        #     tello.curve_xyz_speed(x_coords[i],y_coords[i],z_coords[i],x_coords[i+1],y_coords[i+1],z_coords[i+1],speeds)
        #     time.sleep(0.2) #tune
        tello.land()
        flight_time = tello.get_flight_time()
        print("Flight Time: ", flight_time)
        # emergency stop code
    except KeyboardInterrupt:
        # HANDLE KEYBOARD INTERRUPT AND STOP THE DRONE COMMANDS
        print('keyboard interrupt')
        tello.emergency()
        tello.emergency()
        tello.end()

def get_odometry():
    tello1 = Tello()
    # tello1.connect()
    tello_state = tello1.get_current_state()
    print(tello_state)

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=running_sim, args=())
    t2 = threading.Thread(target=get_odometry, args=())
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    # t2.join()
 
    # both threads completely executed
    print("Done!")
    # running_sim()
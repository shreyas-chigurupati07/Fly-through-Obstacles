# Fly through real objects
In this project a RRT* path planning and minimum snap trajectory generation (motion planning) stack is implemented for the 3D navigation of a DJI Tello Edu quadcopter in simulation (in blender) and is then tested on real quadcopter via NVIDIA Jetson Orin Nano. Additionally a cascaded PID controller gains for position and velocity control are tuned to follow the generated trajectory. 
(Check the full problem statements here [project2a](https://rbe549.github.io/rbe595/fall2023/proj/p2a/) and [project2b](https://rbe549.github.io/rbe595/fall2023/proj/p2b/))

- To run on real quadcopter
	- Set up the tello drone and orin nano
   	- On orin nano clone this repository
   	- Copy the trajectory csv file generated in [Tree-Planning-Through-Trees](https://github.com/ankx22/Tree-Planning-Through-The-Trees) into the repo folder.
   	- Open the `tello_run.py` file and set the appropriate trajectory file name.
   	- Connect to the network of the tello drone and run in `src` folder the following command:
   	  ```
	  python3 tello_run.py
	  ```


## Videos on Quadcopter

Testing on the real quadcopter:

<p float="middle">
	<img src="media/view1.gif" width="350" height="350" title="Front view"/> 
	<img src="media/view2.gif" width="350" height="350" title="Side View"/>
</p>



## References
1. Richter, Charles, Adam Bry, and Nicholas Roy. "Polynomial trajectory planning for aggressive quadrotor flight in dense indoor environments." Robotics Research: The 16th International Symposium ISRR. Springer International Publishing, 2016.



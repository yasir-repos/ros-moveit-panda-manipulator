# ros-moveit-panda-manipulator


AR_week8_test is a ROS package that will automatically generate Cartesian space movements of the end-effector of the Panda robot manipulator. 

Ensure both repositories are downloaded for melodic:

git clone https://github.com/ros-planning/moveit_tutorials.git -b melodic-devel
git clone https://github.com/ros-planning/panda_moveit_config.git -b melodic-devel

To install the file, move the AR_week8_test folder to ~/catkin_ws/src.

Before continuing source your new setup.*sh file:

$ source devel/setup.bash

Use ~/catkin_ws/src/AR_week8_test/src and type:

$ chmod +x square_size_generator.py

$ chmod +x move_panda_square.py

In the workspace, source it using $ source devel/setup.bash, then run $ catkin_make.

Open 4 terminals.

In one terminal: roslaunch panda_moveit_config demo.launch

In another terminal: rosrun AR_week8_test square_size_generator.py

In another terminal: rosrun AR_week8_test move_panda_square.py

To visualise joint position, in the last terminal: rosrun rqt_plot rqt_plot. 

#!/usr/bin/env python

import rospy
import copy
import sys
import moveit_commander
import moveit_msgs.msg
import time
from AR_week8_test.msg import square_length
from math import time

def callback(data):
    try:
        # Define starting configuration
        print  % data.size
        print '------------------- Beginning Starting Configuration -------------------'
        start_conf = [0, -pi / 4, 0, -pi / 2, 0, pi / 3, 0]

        # Move robot to starting configuration
        group.go(start_conf, wait=True)

        # stop() ensures that there is no residual movement
        group.stop()

        print '------------------- Planning Motion Trajectory -------------------'
        # initialise array positions
        waypoints = []

        # get current positions of groups
        wpose = group.get_current_pose().pose

        wpose.position.y += data.length  # First sideways movement in y-direction
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.x += data.length  # Second movement in x-direction
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.y -= data.length  # Third move sideways y-direction
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.x -= data.length  # Finally movement in x-direction
        waypoints.append(copy.deepcopy(wpose))

        (plan, fraction) = group.compute_cartesian_path(
            waypoints,  
            0.01,  # eef_step - cartesian translation, for Cartesian path interpolation at a resolution of 1 cm
            0.0)  # jump_threshold is disabled when set to zero

        # initialise the message for trajectory planning '/move_group/display_planned_path
        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = robot.get_current_state()
        display_trajectory.trajectory.append(plan)
        print '------------------- Showing Planned Trajectory -------------------'
        display_trajectory_publisher.publish(display_trajectory)

        time.sleep(5)
        # Execute  trajectory
        print '------------------- Executing Planned Trajectory -------------------'
        group.execute(plan, wait=True)

    except rospy.ServiceException, e:
        print("Service call failed: %s" % e)


def move_panda_square():
    # initialise moveit commander
    moveit_commander.roscpp_initialize(sys.argv)

    # initialise new rospy node
    rospy.init_node('move_panda_square', anonymous=True)

    # subscribe to square length message and send data to callback
    print '------------------- Waiting for square length -------------------'
    rospy.Subscriber('length', square_length, callback)
    # keeps python from exiting unitl node is stopped
    rospy.spin()


if __name__ == "__main__":
    # initialise robot commander
    robot = moveit_commander.RobotCommander()

    # initialise scene planning interface
    scene = moveit_commander.PlanningSceneInterface()

    # initialise move group commander
    group = moveit_commander.MoveGroupCommander('panda_arm')

    # initialise display trajectory publisher
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=0)
    move_panda_square()



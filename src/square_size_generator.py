#!/usr/bin/env python

import rospy
import random
from AR_week8_test.msg import square_length

def square_size_generator():
    pub = rospy.Publisher('length', square_length, queue_size = 0) #node is publishing to a topic named square
    rospy.init_node('square_size_generator', anonymous = True) #sets name of node to square_size_generator
    rate = rospy.Rate(0.05) #rate is set to 0.05Hz which is 20 seconds
    msg = square_length()
    while not rospy.is_shutdown(): #loops until shutdown
        msg.length = random.uniform(0.05, 0.20)
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()



if __name__ == '__main__':
    try:
        square_size_generator()
    except rospy.ROSInterruptException:
        pass
 

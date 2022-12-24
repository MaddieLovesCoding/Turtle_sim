#!/usr/bin/env python
# coding: utf-8

# ## README
# 
# This is your ROSJect documentation!
# 
# A place to present your ROS Project to the world!
# 
# How to customize it:
# 
# - Open your ROSJect
# 
# - Edit the default jupyter notebook file (**/home/user/notebook_ws/default.ipynb**)
# 
# - Close or wait for it to be saved automatically
# 
# - Your **Readme** will be updated based on your notebook

# In[1]:


print 'Hello from my ROSJect!'


# In[ ]:


#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def rot_tut(radius):
    rospy.init_node('rotate')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=11)
    rate = rospy.Rate(2)
    rot = Twist()
    for y in range(0, 11):
        rot.linear.x = radius
        rot.angular.z = 2
        rospy.loginfo('now radius is=%f', radius)
        pub.publish(rot)
        rate.sleep()


if __name__ == '__main__':
    for j in range(1, 4):
        rot_tut(j)


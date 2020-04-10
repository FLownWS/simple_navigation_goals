#!/usr/bin/env python

import rospy
import actionlib

from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction


class simple_navigation_goals:
    
    def __init__(self):
        super().__init__()

    def goalto(self, x, y, z, OX, OY, OZ, w, theta):
        Client = actionlib.SimpleActionClient ('move_base', MoveBaseAction)
        Client.wait_for_server()
        
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.position.z = z
        goal.pose.orientation.x = OX
        goal.pose.orientation.y = OY
        goal.pose.orientation.z = OZ
        goal.pose.orientation.w = theta

        Client.send_goal(goal)
        pause = Client.wait_for_result()

        if not pause:
            rospy.logerr("Not available right now!")
            rospy.signal_shutdown("Signal down.")

def shutdown(self):
    rospy.signal_shutdown("Process stoped.")    

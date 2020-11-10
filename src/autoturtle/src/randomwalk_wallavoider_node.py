#! /usr/bin/python3

import rospy # sisältää kaikki rosin perusjutut
from geometry_msgs.msg import Twist # ohjausviesti
from turtlesim.msg import Pose # komennot

import random
"""
eka turtle..
"""
# callback-funktio, jossa viestin saatua tutkitaan ja julkaistaan se
def callback(data):
    vel_msg = Twist()
    pose = data
    if pose.x > 10:
        vel_msg.angular.z = 0 # ei kaantymista..
        vel_msg.linear.x = -2 # vaan pakitus
    elif pose.x < 1:
        vel_msg.angular.z = 0 # ei kaantymista..
        vel_msg.linear.x = -2 # vaan pakitus
    elif pose.y > 10:
        vel_msg.angular.z = 0 # ei kaantymista..
        vel_msg.linear.x = -2 # vaan pakitus
    elif pose.y < 1:
        vel_msg.angular.z = 0 # ei kaantymista..
        vel_msg.linear.x = -2 # vaan pakitus
    else: # kun ei olla lahella seinia
        # vel_msg.angular.z = random.randint(-2,2) # joku luku valilta -2..2
        # vel_msg.angular.z = random.randint(-5,5) # joku luku valilta -5..5, isompi kannosvaihtelu
        vel_msg.angular.z = random.randint(-2,5) # joku luku valilta -2..5, kaantyy varmasti vastapaivaan
        vel_msg.linear.x = random.randint(0,2) # etenemää 0..2

    velocity_publisher.publish(vel_msg) # julkaisee viestin

rospy.init_node('turtlebot_auto',anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
# tilaaja.. ottaa yhteytta callback -funktioon
pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose,callback)

# niinkauan kun rossi pyorii ja asiat ok, tehdaan spinnia (muuten poistuisi ohjelmasta)
while not rospy.is_shutdown():
    rospy.spin()

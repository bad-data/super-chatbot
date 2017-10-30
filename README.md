# super-chatbot
A simple and amusing chatbot: Publishes data through ROS nodes, controls arduino! 


# Getting Started
Within the repository is talkingbot.py
Assure that a workspace is created and place it in src.

# In CATKIN workspace:
catkin_make
source devel/setup.bash

# Run chatbot:
roscore

(another terminal)
rosrun rosserial_python serial_node.py /dev/ttyACM0 (whatever dev/ your arduino is)

#!/usr/bin/env python

import sys
from pprint import pprint
import apiai
import json
import string
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('conversation', String, queue_size=20)
rospy.init_node('chatbot', anonymous=True)

if __name__ == '__main__':
	ai = apiai.ApiAI('2b545ec1a2544e20a80cc6c47a3f44ea')
	request = ai.text_request()
	request.session_id= 'api_ai', '<SESSION ID, UNIQUE FOR EACH USER>'

	print('initializing...')	

	while True:
		request = ai.text_request()
		var = raw_input("chat:")
		request.query = var
		response = request.getresponse()
		response_str = response.read()

		response_json = json.loads(response_str)
		robot_response = response_json['result']['fulfillment']['speech']
		print(robot_response)
		pub.publish(var)
		var = ""

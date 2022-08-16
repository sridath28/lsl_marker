#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
#from std_msgs.msg import Float32
#from std_msgs.msg import Int32


import pylsl

from pylsl import StreamInfo, StreamOutlet


info = StreamInfo('pr2_robot', 'Markers', 1, 0, 'string', 'id')
outlet = StreamOutlet(info)

def callback(msg):
		
	outlet.push_sample([msg.data])    
        rospy.loginfo(msg.data)

def main():

	rospy.init_node("lsl_markers", anonymous=True)
	rospy.Subscriber("/lsl_markers", String, callback)

	rospy.spin()


if __name__=='__main__':
  try:
    main()
  except rospy.ROSInterruptException:
    pass

#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class viewer:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/robot/camera1/image_raw_camera", Image, self.callback)

  def callback(self,data):

    cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")  
    cv2.imshow("Camera", cv_image)
    cv2.waitKey(30)
   

def main():
  v = viewer()
  rospy.init_node('viewer_node', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
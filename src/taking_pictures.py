#!/usr/bin/env python
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy as np
import cv2
import cv2.aruco as aruco
import math

# for taking pictures
imag_counter = 0

def convert_color_image(ros_image):
    global imag_counter
    bridge = CvBridge()
    try:
        color_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")

        cv2.namedWindow("Color")
        cv2.imshow("Color", color_image)
        k = cv2.waitKey(10)
        if k % 256 == 32:
            img_name = "opencv_frame_{}.png".format(imag_counter)
            cv2.imwrite(img_name, color_image)
            imag_counter = imag_counter + 1
        
    except CvBridgeError as e:
        print(e)

def detect():
    rospy.init_node("detect", anonymous=True)
    rospy.Subscriber("/usb_cam/image_raw", Image, callback=convert_color_image, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        detect()
    except rospy.ROSInterruptException:
        pass
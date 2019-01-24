import cv2
import numpy as np
from styx_msgs.msg import TrafficLight

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        hsv_image= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

	red_low = np.array([0, 120, 120], np.uint8)
	red_high= np.array([10, 255, 255], np.uint8)

	threshold_img= cv2.inRange(hsv_image, red_low, red_high)

	red_pixels= cv2.countNonZero(threshold_img) 

	if red_pixels > 50:
	  return TrafficLight.RED


        yellow_low= np.array([40.0/360*255, 120, 120],np.uint8)
        yellow_high= np.array([66.0/360*255, 255, 255],np.uint8)
        
	threshold_img= cv2.inRange(hsv_image, yellow_low, yellow_high)

	yellow_pixels= cv2.countNonZero(threshold_img) 

	if yellow_pixels > 50:
	   return TrafficLight.YELLOW



        green_low= np.array([90.0/360*255, 120, 120],np.uint8)
        green_high= np.array([140.0/360*255, 255, 255],np.uint8)

	threshold_img= cv2.inRange(hsv_image, green_low, green_high)

	green_pixels= cv2.countNonZero(threshold_img) 

	if green_pixels > 50:
	   return TrafficLight.GREEN

        return TrafficLight.UNKNOWN

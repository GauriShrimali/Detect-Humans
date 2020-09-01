#PROBLEM STATEMENT 10
#Input: A image contains a human or no human
#Output: Prediction if the image contains a human or not

import cv2 
import imutils 

det = cv2.HOGDescriptor() 
det.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 

image = cv2.imread('img.jpeg') 

(area, _) = det.detectMultiScale(image)

if len(area) == 0:
    print("Image does not contain any humans!")
else:
    print("Image does contain humans!")


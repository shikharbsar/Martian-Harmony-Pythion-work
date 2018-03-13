# import numpy as np
# import cv2
# read = cv2.imread('m812.jpg')
# gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
# ret,binaryImage = cv2.threshold(read, 150, 255, cv2.THRESH_BINARY)
# # detect circles in the image
# circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT,15, 1)
# print circles
# # ensure at least some circles were found
# if circles is not None:
# 	# convert the (x, y) coordinates and radius of the circles to integers
# 	print 3
# 	circles = np.round(circles[0, :]).astype("int")
 
# 	# loop over the (x, y) coordinates and radius of the circles
# 	for (x, y, r) in circles:
# 		# draw the circle in the output image, then draw a rectangle
# 		# corresponding to the center of the circle
# 		cv2.circle(read, (x, y), r, (0, 255, 0), 1)
# 		# cv2.rectangle(read, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
# 	# show the output image
# 	cv2.imshow("output",read)
# 	cv2.waitKey(0)

import cv2
import numpy as np

img = cv2.imread('m812.jpg')
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binaryImage = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# detect circles in the image
im2, contours, hierarchy = cv2.findContours(binaryImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(binaryImage, contours, -1, (0,255,0), 3)
print im2
print 3
# circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 10)
 
# # ensure at least some circles were found
# if circles is not None:
# 	# convert the (x, y) coordinates and radius of the circles to integers
# 	circles = np.round(circles[0, :]).astype("int")
 
# 	# loop over the (x, y) coordinates and radius of the circles
# 	for (x, y, r) in circles:
# 		# draw the circle in the output image, then draw a rectangle
# 		# corresponding to the center of the circle
# 		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
# 		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
# 	# show the output image
# 	cv2.imshow("output", np.hstack([image, output]))
# 	cv2.waitKey(0)b
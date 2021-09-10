
import os
import numpy as np
import cv2

img = cv2.imread("/home/lyleolsen/Pictures/parking_lot.jpg", cv2.IMREAD_COLOR)
grayIMage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel_size = 5
blur_gray = cv2.GaussianBlur(grayIMage,(kernel_size, kernel_size),0)

low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

rho = 1
theta = np.pi/180
cv2.threshold = 15
min_line_length = 50
max_line_gap = 20
line_image = np.copy(img) *0

lines = cv2.HoughLinesP(edges,rho,theta,cv2.threshold,np.array([]),min_line_length,max_line_gap)

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)


line_edges = cv2.addWeighted(img, 0.8, line_image, 1,0)

cv2.imshow("original", img)
cv2.imshow("hls image", grayIMage)
cv2.imshow("lines", line_edges)


cv2.waitKey(0)
 
cv2.destroyAllWindows()
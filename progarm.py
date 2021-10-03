
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def edgeDetection(img, gray, coloring_page):
    edges = cv2.Canny(gray,threshold1=50, threshold2=300)

    cv2.imshow("original",img)
    #cv2.imshow("gray image", gray)
    cv2.imshow("edges", edges)

    reversed = cv2.bitwise_not(edges)
    cv2.imshow("reversed", reversed)

    file_name = coloring_page + ".jpg"

    #status = cv2.imwrite('/home/lyleolsen/Pictures/coloring_pages/' + file_name, reversed)

    #print("Image written to file-system : ",status)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()

def process():
    #file to get
    img = cv2.imread("/home/lyleolsen/Pictures/xmen.jpg", cv2.IMREAD_COLOR)
    grayIMage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #name of the file in the coloring_page folder
    coloringPage = "xmen"
    edgeDetection(img, grayIMage, coloringPage)

process()

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog as fd

def edgeDetection(img, gray, coloring_page):
    #changin
    low_threshold = 22
    ratio = 10
    kernel_size = 15
    max_threshold = low_threshold * ratio
    edges = cv2.Canny(img,low_threshold, max_threshold, kernel_size)
    #original
    #edges = cv2.Canny(gray,threshold1=30, threshold2=100)

    cv2.imshow("original",img)
    #cv2.imshow("gray image", gray)
    cv2.imshow("edges", edges)

    reversed = cv2.bitwise_not(edges)
    cv2.imshow("reversed", reversed)

    file_name = coloring_page + ".jpg"

    status = cv2.imwrite('/home/lyle/Pictures/coloring_pages/' + file_name, reversed)

    #print("Image written to file-system : ",status)
    cv2.waitKey()
    
    cv2.destroyAllWindows()

def flatten_image(img):
    #
    rgb_planes = cv2.split(img)

    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)

    cv2.imshow("original", img)
    cv2.imshow('shadows_out.png', result)
    cv2.imshow('shadows_out_norm.png', result_norm)

    cv2.waitKey()
    cv2.destroyAllWindows()


def process():

    imageLocation = fd.askopenfilename()
    #file to get
    # "/home/lyle/Pictures/spidey2.jpg"
    img = cv2.imread(imageLocation, cv2.IMREAD_COLOR)
    grayIMage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian_img = cv2.Laplacian(grayIMage,cv2.CV_64F)
    sobelx = cv2.Sobel(grayIMage,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(grayIMage,cv2.CV_64F,0,1,ksize=5)


    #name of the file in the coloring_page folder
    image_location_split = imageLocation.split("/")
    len_array = len(image_location_split)
    file_name = image_location_split[len_array -1]
    file_name_split = file_name.split('.')
    save_file_name = file_name_split[0]

    coloringPage = save_file_name
    edgeDetection(img, grayIMage, coloringPage)


process()
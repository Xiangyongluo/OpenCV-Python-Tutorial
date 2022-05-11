#!/usr/bin/python

'''
This example illustrates how to use Hough Transform to find lines

Usage:
    houghlines.py [<image_name>]
    image argument defaults to ../data/pic1.png
'''


# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math

if __name__ == '__main__':
    print(__doc__)

    try:
        fn = sys.argv[1]
    except IndexError:
        fn = "../data/pic1.png"

    src = cv2.imread(fn)
    dst = cv2.Canny(src, 50, 200)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 40, np.array([]), 50, 10)
    a,b,c = lines.shape
    for i in range(a):
        cv2.line(cdst, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)

    cv2.imshow("source", src)
    cv2.waitKey(0)

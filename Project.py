import cv2
from PIL import Image
import numpy as np
perfwallimg = cv2.imread("pref.jpg")
crackwall = cv2.imread("pref.jpg")
if perfwallimg is None:
    print("Wrong path")
else:
    perfwallimg = cv2.resize(perfwallimg, dsize = (128,128))
if crackwall is None:
    print("Wrong path")
else:
    crackwall = cv2.resize(crackwall, dsize = (128,128))
if perfwallimg.shape == crackwall.shape:
    diff = cv2.subtract(perfwallimg, crackwall)
    b,g,r = cv2.split(diff)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The image are complete equal")
    else:
        print("The first image is perfect wall image\n")
        print("Perfect_wall----Image----open----\n")
        image0 = Image.open("pref.jpg")
        image0.show()
        print("Second image is crack wall image\n")
        print("Crcak_wall----Image----open----\n")
        Image1 = Image.open("crack.jpg")
        Image1.show()

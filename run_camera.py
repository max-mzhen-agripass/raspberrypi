import cv2
import keyboard
import numpy as np
import time

"""
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# choose parameters
width = 2592
height = 1944
fourcc = cv2.VideoWriter.fourcc('M', 'J', 'P', 'G')  # format

# set parameters
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FOURCC, fourcc)
"""

start_time = time.time()
run = False

# draw black box
im = np.zeros((512,512,3), np.uint8)

print("READY")

while True:

    if run:
        # retval, im = camera.read()
        color = int((1000*(time.time() - start_time))%255)
        print(color)
        im.fill(color)
        cv2.imshow("image", im)
        cv2.waitKey(1)

    if not run and keyboard.is_pressed("f"):
        print("You pressed 'f'. Starting captures")
        run = True

    elif run and keyboard.is_pressed("g"):
        print("You pressed 'g'. Pausing captures")
        run = False

    elif keyboard.is_pressed("d"):
        print("You pressed 'd'. Exiting program...")
        exit()

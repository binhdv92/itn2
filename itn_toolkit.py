# -*- coding: utf-8 -*-
# In[] Import
import cv2
from datetime import datetime
import os
# import argparse


# In[] Declare
def get_picture_name(PICTURE_PERFIX_NAME="500112800"):
    dt = datetime.now()
    dtstr=f"{dt}"
    dtstr=dtstr.replace(" ","_")
    dtstr=dtstr.replace(":","-")
    IMAGE_NAME=f"{PICTURE_PERFIX_NAME}_{dtstr}.jpg"
    # print(IMAGE_NAME)
    IMAGE_NAME=os.path.join("images",IMAGE_NAME)
    return IMAGE_NAME
# cv2.ROTATE_90_CLOCKWISE
# In[]
cap = cv2.VideoCapture(0)


while True:
    ret,frame = cap.read()
    frame = cv2.rotate(frame,cv2.ROTATE_180)
    
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    
    if key == ord("q"):
        print("exit programe")
        break
    elif(key == ord("s")):
        IMAGE_NAME=get_picture_name(PICTURE_PERFIX_NAME="500112800")
        print(f"Save {IMAGE_NAME} to disk")
        cv2.imwrite(IMAGE_NAME,frame)
    

cv2.waitKey(0)
cv2.destroyAllWindows()
    
    


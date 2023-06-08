from pynput.keyboard import Key, Controller
from unittest import result
import cv2
import numpy as np
import mediapipe as mp
from random import *
from matplotlib import pyplot as plt
import time

left = [Key.left, True, 0]
right = [Key.right, True, 0]
up = [Key.up, True, 0]
down = [Key.down, True, 0]
enter = [Key.enter, True, 0]
XButton = ["x",True,0]
ZButton = ["z",True,0]
TextColor = (255,255,255)



cap = cv2.VideoCapture(1)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4,2)
handCenter = 0
Dotsinimage = []

class Get:
    def __init__():
        self.boxlist = []
    #This is how the computer finds the hit box
    def hitbox(Leftx,Rightx,topy,bottomy):
        for gettinghandsfromlist in Dotsinimage:
            if gettinghandsfromlist[0] > Leftx and gettinghandsfromlist[0] < Rightx and gettinghandsfromlist[1] > topy and gettinghandsfromlist[1] < bottomy:
                del Dotsinimage[:]
                return "bacon"
        del Dotsinimage[:]
        return "no bacon"   


    def BoxPlacment(self,NumberOfBoxes):
        boxx = randint(1,400)
        boxy = randint(1,400)
        for i ,j in self.BoxPlacment:
            if i < boxx and i > boxx + 50:
                pass

keyboard = Controller()
#This works with the cleanup def. 
def Input(Letter):
    if Letter[1] == True:
        key = Letter[0]
        keyboard.press(key)
        Letter[1] = False
        Letter[2] = time.time()
#This makes sure the button isn't presses to fast. 
def cleanup():
    for CheckPress in [left,right,up,down,enter,XButton,ZButton]:
        if CheckPress[1] == False:
            CheckTime = time.time()
            if CheckTime - CheckPress[2] > 0.15:
                    keyboard.release(CheckPress[0])
                    CheckPress[1] = True



while True:
    success, image = cap.read()
    image = cv2.flip(image,1)
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks

    #Getting all the hand placments
    if multiLandMarks:
        handList = []
        for handLms in multiLandMarks:
            
            for idx, lm in enumerate(handLms.landmark):

              h, w, c = image.shape
              cx, cy = int(lm.x * w), int(lm.y * h)
              handList.append((cx, cy))
                #This finds the middle finger knuckle 
              if idx == 9:
                Dotsinimage.append((cx,cy))
                print((cx,cy))
                cv2.circle(image, (cx,cy), 10, (255, 255, 0), cv2.FILLED)    
                # Checking if hand is in box
            for checking in handList:    
                if cx > StartButtonBeings[1] and cy < StartButtonEnds[1]:
                    if cx > StartButtonBeings[0] and cx < StartButtonEnds[0]:
                        Input(enter)
                if cy > 25 and cy < 100:
                    if cx > LeftArrowBegin[0] and cx < LeftArrowEnd[0]:
                        #print("left")
                        Input(left)
                    elif cx > RightAarowBegins[0] and cx < RightAaroEnds[0]:
                        #print("right")
                        Input(right)
                if cy > 50 and cy < 125:
                    if cx > DownArrowBegins[0] and cx < DownArrowEnds[0]:
                        #print("down")
                        Input(down)
                    elif cx > UpArrowBeings[0] and cx < UpArrowEnds[0]:
                        #print("up")
                        Input(up)
                if cy > 75 and cy < 150:
                    if cx > AButtonBegins[0] and cx < AButtonEnds[0]:
                        #print("A")
                        Input(XButton)
                    elif cx > BButtonBegins[0] and cx < BButtonEnds[0]:
                        Input(ZButton)
                        #print("B")
    #This is the placment of all the boxes
    Ticcness = 2
    LeftArrowBegin = (200,25)
    LeftArrowEnd = (275,100)
    RightAarowBegins = (375,25)
    RightAaroEnds = (450,100)
    UpArrowBeings = (475,50)
    UpArrowEnds = (550,125)
    DownArrowBegins = (100,50)
    DownArrowEnds = (175, 125)  #225 - 300
    AButtonBegins = (575,75)
    AButtonEnds = (650,150)
    BButtonBegins = (0,75)
    BButtonEnds = (75,150)
    StartButtonBeings = (300,0)
    StartButtonEnds = (350, 75)
    #This displays the letters and boxes
    cv2.putText(image, "Right", (RightAarowBegins[0], 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, TextColor)
    cv2.putText(image, "Left", (LeftArrowBegin[0], 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, TextColor)
    cv2.putText(image, "up", (UpArrowBeings[0], 75), cv2.FONT_HERSHEY_SIMPLEX, 1.0, TextColor)
    cv2.putText(image, "down", (DownArrowBegins[0], 75), cv2.FONT_HERSHEY_SIMPLEX, 1.0, TextColor)
    cv2.putText(image, "B", (BButtonBegins[0], 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, TextColor)
    cv2.putText(image, "A", (AButtonBegins[0], 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, TextColor)
    cv2.putText(image, "Start", (StartButtonBeings[0], 25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, TextColor)
    cv2.rectangle(image, LeftArrowBegin, LeftArrowEnd,(0,255,0),Ticcness)
    cv2.rectangle(image, RightAarowBegins,RightAaroEnds ,(0,0,225),Ticcness)
    cv2.rectangle(image, UpArrowBeings,UpArrowEnds ,(255,0,0),Ticcness)
    cv2.rectangle(image, DownArrowBegins,DownArrowEnds ,(0,0,0),Ticcness)
    cv2.rectangle(image, AButtonBegins,AButtonEnds ,(255,255,255),Ticcness)
    cv2.rectangle(image, BButtonBegins,BButtonEnds ,(255,0,255),Ticcness)
    cv2.rectangle(image, StartButtonBeings, StartButtonEnds, (125,125,125), Ticcness)
    
    
    cv2.imshow("Counting number of fingers", image)
    cleanup()
    cv2.waitKey(1)

import cv2
from numpy import *
import time
import yagmail

# the idea is show an image of what to do then have a timer 
# control when the next exorsis starts. Try and add voice control 
# to go to the next exorsis.
# I'm thinking of putting the exorsises in an oray something like {name:[image,time]}

def imagesize(ImagePath,ImageTime):
    

    #path = ImagePath
    c = cv2.imread(ImagePath)
    height, width = c.shape[:2]
    cv2.namedWindow('jpg', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('jpg', width, height)
    cv2.imshow('jpg', c)
    Itime = time.time()

    cv2.waitKey(ImageTime)
    
    #time.sleep(1)
    cv2.destroyWindow('jpg')
def SendEmail():


    user = 'your_username@gmail.com'
    app_password = 'your_app_password' # a token for gmail
    to = 'your_recipent@gmail.com'

    subject = 'test subject 1'
    content = ['mail body content','pytest.ini','test.png']

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully')    

def runningWorkout():
    workingout = [["Testone.jpg",3000]]
    for I,O in workingout:
        imagesize(I,O)
runningWorkout()

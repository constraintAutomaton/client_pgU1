import numpy as np
import cv2

def image():
    img = cv2.imread('Kodak_1.jpg')
    
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    upperRed = np.array([175/2,100*(255/100),100*(255/100)])
    lowerRed = np.array([75/2,100*(255/100),100*(255/100)])
    
    mask = cv2.inRange(hsvImg,lowerRed,upperRed)
    res = cv2.bitwise_and(img,img,mask=mask)
    
    posColor = np.where(mask!=0)
    print(a)
    
    #cv2.imshow('res',res)
    #cv2.imshow('mask',mask)
    #cv2.imshow('img',img)
    cv2.imshow('a',a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def video():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        hsvFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        lower_red = np.array([170,255,255])
        upper_red = np.array([180,255,255])

        mask = cv2.inRange(hsvFrame, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()    
    
    
video()
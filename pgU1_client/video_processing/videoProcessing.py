import numpy as np
import cv2
import time
import math
import os


class VideoProcessing():
    def __init__(self, cameraPort=0,debug=False):
        self.cameraPort = cameraPort
        self.pastCentroidX = 1
        self.pastCentroidY = 1
        self.debug = debug
    def cameraConfig(self):
        self.cap = cv2.VideoCapture(self.cameraPort)

    def laserColor(self):

        with open(os.path.join('calibration','laserColor.txt'), 'r') as file:

            text = file.readlines()
            color = []
            for line in text:
                if line != '':
                    start = line.find(':') + 1
                    end = line.find(';')
                    substring = line[start:end]
                    hsv = substring.split(',')

                    color.append([float(hsv[0]), float(hsv[1]), float(hsv[2])])
                else:
                    break

            self.upperRedUp = color[0]
            # hsv range are h:0-360, s:0-100, v:0-100 and openCv hsv range are h:0-180, s:0-255, v:0-255
            self.upperRedUp[0] = self.upperRedUp[0] / 2
            self.upperRedUp[1] = self.upperRedUp[1] * (255 / 100)
            self.upperRedUp[2] = self.upperRedUp[2] * (255 / 100)
            self.upperRedUp = np.array(self.upperRedUp)
            
            self.upperRedLow = color[1]
            self.upperRedLow[0] = self.upperRedLow[0] / 2
            self.upperRedLow[1] = self.upperRedLow[1] * (255 / 100)
            self.upperRedLow[2] = self.upperRedLow[2] * (255 / 100)
            self.upperRedLow = np.array(self.upperRedLow)
            
            self.lowerRedUp = color[2]
            self.lowerRedUp[0] = self.lowerRedUp[0] / 2
            self.lowerRedUp[1] = self.lowerRedUp[1] * (255 / 100)
            self.lowerRedUp[2] = self.lowerRedUp[2] * (255 / 100)
            self.lowerRedUp = np.array(self.lowerRedUp)
            
            self.lowerRedLow = color[3]
            self.lowerRedLow[0] = self.lowerRedLow[0] / 2
            self.lowerRedLow[1] = self.lowerRedLow[1] * (255 / 100)
            self.lowerRedLow[2] = self.lowerRedLow[2] * (255 / 100)
            self.lowerRedLow = np.array(self.lowerRedLow)
            
    def configLaserColor(self, upperRedUp, upperRedLow, lowerRedUp, lowerRedLow):

        text = 'upper Red Up :{};\nupper Red low:{};\nlower Red Up :{};\nlower Red low:{};'.format(
            upperRedUp, upperRedLow, lowerRedUp, lowerRedLow)
        print(text)
        with open('calibration\laserColor.txt', 'w') as file:
            file.write(text)

    def runCamera(self):
        self.laserColor()
        while True:
            self.ret, self.frame = self.cap.read()
            self.distanceDetection()
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
        self.cap.release()

    def distanceDetection(self):
        

        hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

        upperRedUp = np.array(self.upperRedUp)
        lowerRedUp = np.array(self.lowerRedUp)
        maskUp = cv2.inRange(hsvFrame, lowerRedUp, upperRedUp)

        lowerRedLow = np.array(self.lowerRedLow)
        upperRedLow = np.array(self.upperRedLow)
        maskLow = cv2.inRange(hsvFrame, lowerRedLow, upperRedLow)

        mask = cv2.bitwise_or(maskUp, maskLow)
        res = cv2.bitwise_and(self.frame, self.frame, mask=mask)

        laserPos = np.nonzero(mask)
        
        centroidY = round(np.average(laserPos[0]))
        centroidX = round(np.average(laserPos[1]))
        if math.isnan(centroidX) or math.isnan(centroidY):
            centroidX = self.pastCentroidX
            centroidY =self.pastCentroidY
        else:
            centroidX,centroidY = (int(centroidX),int(centroidY))
        centerFrameY = int(round(mask.shape[0]/2))
        centerFrameX = int(round(mask.shape[1]/2))

        cv2.circle(self.frame, (centerFrameX, centerFrameY), 5, (255, 0, 0),-1)
        cv2.circle(self.frame, (centroidX, centroidY), 5, (0, 0, 255),-1)
        if self.debug == True:
            cv2.imshow('frame', self.frame)
            cv2.imshow('mask',mask)
            cv2.imshow('res',res)             
                       
    def killCamera(self):

        cv2.destroyAllWindows()
        self.cap.release()

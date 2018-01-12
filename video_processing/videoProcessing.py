import numpy as np
import cv2
import time

#np.set_printoptions(threshold=np.nan)
class VideoProcessing():
    def __init__(self,cameraPort=0,):
        self.cameraPort = cameraPort 
    def cameraConfig(self):
        self.cap = cv2.VideoCapture(self.cameraPort)
            
    def laserColor(self):
        
        with open(r'calibration\laserColor.txt','r') as file:
            
            text = file.readlines()
            color = []
            for line in text:
                if line!='':
                    start = line.find(':')+1
                    end = line.find(';')
                    substring = line[start:end]
                    hsv = substring.split(',')
                    
                    color.append([float(hsv[0]),float(hsv[1]), float(hsv[2]) ])
                else:
                    break            
                
            self.upperRedUp = color[0]
            # hsv range are h:0-360, s:0-100, v:0-100 and openCv hsv range are h:0-180, s:0-255, v:0-255
            self.upperRedUp[0]  = self.upperRedUp[0]/2
            self.upperRedUp[1] = self.upperRedUp[1]*(255/100)
            self.upperRedUp[2] = self.upperRedUp[2]*(255/100)
            
            self.upperRedLow = color[1]    
            self.upperRedLow[0]  = self.upperRedLow[0]/2
            self.upperRedLow[1] = self.upperRedLow[1]*(255/100)
            self.upperRedLow[2] = self.upperRedLow[2]*(255/100)
            
            self.lowerRedUp= color[2]    
            self.lowerRedUp[0]  = self.lowerRedUp[0]/2
            self.lowerRedUp[1] = self.lowerRedUp[1]*(255/100)
            self.lowerRedUp[2] = self.lowerRedUp[2]*(255/100) 
            
            self.lowerRedLow = color[3]    
            self.lowerRedLow[0]  = self.lowerRedLow[0]/2
            self.lowerRedLow[1] = self.lowerRedLow[1]*(255/100)
            self.lowerRedLow[2] = self.lowerRedLow[2]*(255/100)
        
    def configLaserColor(self,upperRedUp,upperRedLow,lowerRedUp,lowerRedLow):
        
        text = 'upper Red Up :{};\nupper Red low:{};\nlower Red Up :{};\nlower Red low:{};'.format(upperRedUp,upperRedLow,lowerRedUp,lowerRedLow)
        print(text)
        with open('calibration\laserColor.txt','w') as file:
            file.write(text)
    def runCamera(self):      
        while True:
            self.ret, self.frame = self.cap.read()
            self.distanceDetection()
            cv2.imshow('frame',self.frame)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
    
        cv2.destroyAllWindows()
        cap.release()                     
            
    def distanceDetection(self):
        self.laserColor()
        
        hsvFrame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)
         
        upperRedUp = np.array(self.upperRedUp)
        lowerRedUp = np.array(self.lowerRedUp)       
        maskUp = cv2.inRange(hsvFrame,lowerRedUp,upperRedUp)
              
        lowerRedLow = np.array(self.lowerRedLow)
        upperRedLow = np.array(self.upperRedLow)
        maskLow = cv2.inRange(hsvFrame,lowerRedLow,upperRedLow)
        
        
        mask = cv2.bitwise_or(maskUp,maskLow)
        res = cv2.bitwise_and(self.frame,self.frame,mask=mask)        
        
        laserPos = np.nonzero(mask)
        
        
        centroidY = int(round(np.average(laserPos[0])))
        centroidX = int(round(np.average(laserPos[1])))
            
        centerFrameY = mask.shape[0]
        centerFrameX = mask.shape[0]
        
        cv2.circle(self.frame,(centerFrameX,centerFrameY),25,(0,0,255))  
        
    def killCamera(self):
        
        cv2.destroyAllWindows()
        self.cap.release()        
            
            
            
            
        
        
        
        
        



import numpy as np
import cv2
import math


def image():
    # cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    img = cv2.imread('IMG_20180105_174151466.jpg')
    imgS = cv2.resize(img, (600, 600), interpolation=cv2.INTER_AREA)

    #r = cv2.selectROI(imgS)
    #imgS = imgS[10:301,78:365]

    hsvImg = cv2.cvtColor(imgS, cv2.COLOR_BGR2HSV)

    upperRedUp = np.array([360 / 2, 100 * (255 / 100), 100 * (255 / 100)])
    lowerRedUp = np.array([350 / 2, 20 * (255 / 100), 30 * (255 / 100)])
    maskUp = cv2.inRange(hsvImg, lowerRedUp, upperRedUp)

    lowerRedLow = np.array([11 / 2, 57 * (255 / 100), 63 * (255 / 100)])
    upperRedLow = np.array([15 / 2, 100 * (255 / 100), 100 * (255 / 100)])
    maskLow = cv2.inRange(hsvImg, lowerRedLow, upperRedLow)

    mask = cv2.bitwise_or(maskUp, maskLow)
    res = cv2.bitwise_and(imgS, imgS, mask=mask)

    laserPos = np.nonzero(mask)

    centroidY = int(round(np.average(laserPos[0])))
    centroidX = int(round(np.average(laserPos[1])))

    cv2.circle(res, (centroidX, centroidY), 25, (0, 0, 255))

    print(laserPos)

    resS = cv2.resize(res, (600, 600), interpolation=cv2.INTER_AREA)

    cv2.imshow('res', resS)
    cv2.imshow('mask', mask)
    cv2.imshow('img', imgS)
    # print(r)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def video():
    cap = cv2.VideoCapture(0)

    while True:
        print('ok')
        ret, frame = cap.read()
        #hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #upperRedUp = np.array([360 / 2, 100 * (255 / 100), 100 * (255 / 100)])
        #lowerRedUp = np.array([350 / 2, 31 * (255 / 100), 50 * (255 / 100)])
        #maskUp = cv2.inRange(hsvFrame, lowerRedUp, upperRedUp)

        #lowerRedLow = np.array([11 / 2, 57 * (255 / 100), 63 * (255 / 100)])
        #upperRedLow = np.array([15 / 2, 100 * (255 / 100), 100 * (255 / 100)])
        #print(upperRedLow)
        #maskLow = cv2.inRange(hsvFrame, lowerRedLow, upperRedLow)

        #mask = cv2.bitwise_or(maskUp, maskLow)
        #res = cv2.bitwise_and(frame, frame, mask=mask)

        #laserPos = np.nonzero(mask)

        #centroidY = int(round(np.average(laserPos[0])))
        #centroidX = int(round(np.average(laserPos[1])))

        #cv2.circle(res, (centroidX, centroidY), 25, (0, 0, 255))

        #cv2.imshow('frame', frame)
        #cv2.imshow('mask',mask)
        #cv2.imshow('res',res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()


video()

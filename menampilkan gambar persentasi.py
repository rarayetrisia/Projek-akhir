import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from imutils.video import FPS
from imutils.video import WebcamVideoStream
import time


#var
lsgmb = 0
hs, ws = int(150), int(200)
folder = "Presentation"
width, height = 1280, 720
gesture = 400
jeda = False
delay = 15
counter = 0

time.sleep(2.0)
fps = FPS().start()


#set up kamera
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

#menampilkan list gambar
pathgmb = sorted(os.listdir(folder),key=len)
print(pathgmb)


#handtracking
deteksi = HandDetector(detectionCon = 0.8, maxHands = 1)

while True:

#import image
    success, gmb = cap.read()
    gmb = cv2.flip(gmb,1) #mirror
    pathfullgmb = os.path.join(folder, pathgmb[lsgmb])
    gmbcurrent = cv2.imread(pathfullgmb)

#deteksi tangan
    hands, gmb = deteksi.findHands(gmb) 
    #garis pembatas gesture
    cv2.line(gmb,(0, gesture), (width, gesture), (100,200,40),10)

    if hands and jeda is False :
        hand = hands[0]
        cx, cy = hand['center']
        lmList = hand["lmList"]
        jari = deteksi.fingersUp(hand)
        print(jari)

        #area pointer
        # indexjari = lmList[8][0],lmList[8][1]
        nilai_x = int(np.interp(lmList[8][0],[width//2,width],[0,width]))
        nilai_y = int(np.interp(lmList[8][1], [200, height-200], [0, height]))
        indexjari = nilai_x, nilai_y


        if cy <= gesture:
            #gesture 1 geser kiri
            if jari == [1,0,0,0,0]:
                jeda = True
                if lsgmb > 0:
                    lsgmb -= 1
            
            #gesture 2 geser kanan
            if jari == [0,0,0,0,1]:
                jeda = True
                if lsgmb < len (pathgmb)-1:
                    lsgmb += 1

        ##gesture 3 gerak pointer
        if jari == [0,1,1,0,0]:
            cv2.circle(gmbcurrent,indexjari, 10, (0,255,0),cv2.FILLED)
                    
    #tombol virtual
    if jeda:
        counter +=1
        if counter > delay:
            counter = 0
            jeda = False
            
#webcam kecil di slide
    gmbkecil = cv2.resize(gmb,(ws, hs))
    h,w,_= gmbcurrent.shape
    gmbcurrent[0:hs, w - ws: w]= gmbkecil

    cv2.imshow("presenter", gmb)
    cv2.imshow("Slide", gmbcurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    fps.update()

WebcamVideoStream(src=cameranum).stop()
fps.stop()
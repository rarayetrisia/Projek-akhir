import cv2
import os

#variabel
# width, height = 1280,720
folder = "Presentation"
#camera setup
cap = cv2.VideoCapture(0)
# cap.set(3, width)
# cap.set(4, height)

#get the list of presentation gmb
pathgmb = sorted(os.listdir(folder),key=len)
print(pathgmb)

#var
nomorgmb = 0
while True:
    # #menmpilkan gambar pada folder
    # sukses, img = cap.read()
    pathfullgmb = os.path.join(folder, pathgmb[nomorgmb])
    gmbcurrent = cv2.imread(pathfullgmb)


    # cv2. imshow("gmb", img)
    cv2. imshow("Slide", gmbcurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
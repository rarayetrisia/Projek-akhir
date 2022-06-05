from cvzone.HandTrackingModule import HandDetector
import cv2



cap = cv2. VideoCapture(0)
deteksi = HandDetector(detectionCon=0.5, maxHands = 1)


while True:
    sukses, gmb = cap.read()
    hands, gmb = deteksi.findHands(gmb)
    # gmb= cv2.flip(gmb,1)
    cv2.imshow("gambar", gmb)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
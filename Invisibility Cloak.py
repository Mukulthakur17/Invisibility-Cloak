import cv2
import numpy as np 

cap = cv2.VideoCapture('HariPutr.mp4')

for i in range(60):
    ret, background = cap.read()
    if ret == False:
        continue

while cap.isOpened:
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lb = np.array([155, 80, 135])
    ub = np.array([185, 225, 255])
    mask = cv2.inRange(hsv, lb, ub)

    #Dilate Filter
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations = 1)

    #Closing Filter
    kernal = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

    mask1 = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(background, background, mask = mask) 
    res2 = cv2.bitwise_and(frame, frame, mask = mask1) 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0) 
  
    cv2.imshow("HariPutr", final_output) 

    if cv2.waitKey(25) == 27 :
        break


cap.release()
cv2.destroyAllWindows()

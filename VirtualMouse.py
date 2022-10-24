import cv2 as c
import mediapipe as mp
from mediapipe.python.solutions import drawing_utils
import pyautogui

#starts camera capture
cap = c.VideoCapture(0)

handDetector = mp.solutions.hands.Hands()

screenWidth, screenHeight = pyautogui.size()

y1 = 0

while True:

    ret, frame = cap.read()
    frame = c.flip(frame,1)
    height,width,_=frame.shape
    rgbframe = c.cvtColor(frame,c.COLOR_BGR2RGB)

    out = handDetector.process(rgbframe)
    hands = out.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*width)
                y=int(landmark.y*height)

                if id==8:
                    c.circle(frame,(x,y),5,(255,0,0),-1)
                    x1 = screenWidth/width*x
                    y1 = screenHeight/height*y
                    pyautogui.moveTo(x1,y1)
                if id==4:
                    c.circle(frame,(x,y),5,(255,0,0),-1)
                    x2 = screenWidth/width*x
                    y2 = screenHeight/height*y

                    if abs(y1 - y2) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)



    c.imshow('potato', frame)

    if c.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
c.destroyAllWindows()
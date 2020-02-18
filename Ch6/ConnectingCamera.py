import cv2
import time

cap = cv2.VideoCapture(0)



if not (cap.isOpened()):
    print('Could not open video device')
x = 0
while(True):
    ret, frame = cap.read()
    cv2.imshow('preview',frame)
    time.sleep(1)
    cv2.imwrite(f'./images/cap{x}.jpg', frame) 

    x = x+1 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

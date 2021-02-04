import cv2
from time import sleep

debugging = True
classifier = \
cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    if not video.isOpened():
        print('Waiting for Camera.')
        sleep(5)
        pass

    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(gray,minNeighbors=5,minSize=(100, 100))
    if debugging:
      for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
     cv2.imshow('Video', frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    if len(faces) > 0:
      # Your advanced code here
      pass
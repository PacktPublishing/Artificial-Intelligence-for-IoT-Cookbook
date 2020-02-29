One advantage of using OpenCVs implementation of visual neural networks is that they are avaialble on different platforms.  For the sake of clarity and brevity we are using Python on a environment that has Python installed.  But the same results could be used with OpenCV's C++ implemenation on a ARM-CortexM3 or OpenCV's Java implementation on an Android system.  In this recipie we are going to use a face detection Neural Network that OpenCV implenented based on Cafee.  The output of this recipie is a window on the PC that has the image with bouding boxes around the face.

Getting ready

To run this recipe you will need a web camera attached to your device or pc.  You will need to install OpenCV, Numpy, and Imutils if you have already not done so. Installing OpenCV can be challenging on very constrained devices.  There are several ways you can attempt to do it if you are not able to natively on a device.  Many devices with extra storagespace will allow you to use the disk as swap space for the memory.  If the device in question supports dockerizaton then you can compile on a computer and run the container on the device.

How to do it
1. Import libraries
import cv2
import numpy as np
import imutils

2. Get Neural Network and Camera
net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
cap = cv2.VideoCapture(0)

3. Getting the restults
def FaceNN(frame):
    frame = imutils.resize(frame, width=300, height=300)
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (103.93, 116.77, 123.68))
    net.setInput(blob)
    detections = net.forward()

4. Drawing bounding boxes

  for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence < .8:
            continue

        # compute the (x, y)-coordinates of the bounding box for the
        # object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # draw the bounding box of the face along with the associated
        # probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
                      (0, 0, 300), 2)
        cv2.putText(frame, text, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 300), 2)

5. Return the image with bounding boxes

  return frame

6. Main loop

while True:
    ret, frame = cap.read()
    image = FaceNN(frame)
    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

7. Clean up

cap.release()
cv2.destroyAllWindows()

How it works

After importing our libraries we import the pretrained face detection model into our net variable.  We then open the first camera (0) that we find.  Then it is time for the FacNN to predict the image and draw the bounding box.  We are passing in the image frame.  Then we shrink the image to an appropriate demension.  We then use imutils to resize our large image from the camera.  We then set the image in the newtork and get the face detections.  Next we get the face detections and parse out the confidence that the object it finds is really a face.  In our case we are using a .8 or 80% threshhold.  We are filtering out low confidance faces.  We then draw bounding boxes around the faces and putiing confidance text on the boxes.  We then return those images to our main while True loop and display them on the screen.  We also wait for a q key to quit.  Finally we release the camera and destry the UI window.



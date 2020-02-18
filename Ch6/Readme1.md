Introduction

Computer vision has come a long way in recent years.  Unlike many other forms of machine learning that require complex analysis the vast majority of computer vision problems come from simple RGB cameras.  Machine learning frameworks such as Keras and OpenCV have standard high accuracy neural networks built in.  A few years ago implementing facial recoginition neural net was complex and challenging to set up in Python let alone on a high speed device using C++.  Today OpenCV's can expose both the camera and a deep neural network algorithm on a bare metal device.  In this capter we are going to talk about implementing Computer vision on a variety of devices. Some constrained and some with GPU support.


Connecting Cameras through OpenCV
Labeling dataset
Using Microsoft’s Object Detection API to quick start your project.
Using Transfer Learning for Object Detection
Real-time object detection on GPU enabled devices with Yolo
Classifying Images on constrained devices with HAAR Cascade



Connecting Cameras through OpenCV

Connecting a camera through OpenCV is fairly strait forward.  The issue is often in installing OpenCV.  OpenCV installs easily on a desktop computer but on more constrained devices may take exra work. In a Raspberry Pi 3, for example, you may need to enable swap space. Which allows the system to use the SD card as a tepory memeory store.  Depending on the device there are various instuctions online on how to get OpenCV onto a challenging device.

In this recipie we will connect OpenCV to a camera and then stream it to the desktop application.  In future recipies we will assume knowledge of this and breeze by the explination of what is going on.

Getting Ready
The only thing needed for this recipie is a computer and a camera.  Most laptops have built in cameras but for a desktop comuter or a SBC like a Raspberry Pi or LattePanda you will need a USB web camera.  The next step is to install OpenCV.

Next you will need to install OpenCV. As mentioned earlier there are ways of getting OpenCV on costraied devices.  These are all unique to the device in question.  For the sake of simpliccity we will install it for Windows/Linux/Mac.

There are 3 different libraries we can pip install opencv-contrib-python, for all of the OpenCV extras, opencv-python for a faster but shorter list of features, and finally opencv-cython for a faster Python experience.

For this book I would recommend performing the following command 
```
pip install opency-contrib-python
```
How to do it


1. Import OpenCV
import cv2

2. Select the Camera
cap = cv2.VideoCapture(0)

3. Check if the camera is available
if not (cap.isOpened()):
    print('Could not open video device')

4. Capture, save and show frames
while(True):

    ret, frame = cap.read()
    cv2.imshow('preview',frame)
    time.sleep(1)
    cv2.imwrite(f'./images/cap{x}.jpg', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

5. Release Camera 
cap.release()
cv2.destroyAllWindows()


How it works
In this recipie first we import OpenCV.  We then select the first camera it finds (camera(0)).  If we were looking for the second camera it found then we would incriment the camera number (camera(1)).  Next we check if the camera is available. There can be several reasons.  First it could be opened by somthing else.  You could, for example, open the camera in a different application this would prevent the python application from attaching.  Another common issue is that the releasing the camera step does not get executed and the camera needs to be reset.  Next we capture the fideo frames and present them on screen until someone presses the q key.  Fianally after someone has exited the application we release the camera and close the open window.

Wait there is more
OpenCV has many tools to write text to the screen or draw bounding boxes around an identified object.  In addition it has the ability to down sample or change a RGB image to black and white.  These are techniques machine learning engineers to on constrained devices to allow them to operate efficently.  


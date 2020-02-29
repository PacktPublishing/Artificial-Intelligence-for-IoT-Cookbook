Using Microsoft’s Custom vision to label your images.
Microsofts Cognitive Services offer a one-stop-shop for everything you need for training images and deploying models.  First it provides a way of uploading images.  Then it has a UI for drawing bounding boxes around images, finally it allows you to deploy and exposes an API endpoint you can use for classifiying your images.  

Getting started
To use the Microsoft's custom vision service you will need an Azure subscription.  Then you will need to spin up a new custom vision project.  There is a free tier for testing out small models and a paid tier for larger models and serving models at scale.  After creating the Custom Vision project in the Azure portal you will see 2 new project in the resource group.  The first will be for training and the second will have a "-prediction" appended to the name which will be used for the predictions.  You will then need to go into both services and and get the service key and API endpointa from keys tab in the portal. 

Then you will need images of what you are classifying. In our case we are idenfying beverages in an environment with led and carcigin exposre. If you have completed the last recipie you will have a capturing images at one second intervals.  To make an object dection model in Cognitive Services you will need at least 30 images of each thing you are trying to classify.  More images will improve accuracy. To get good accuracy you should very the light, background, angle, size, type, and indvidual and grouped images of the objects.

You also need to install Microsofts cognitive services computer vision package.  To do that:

```
pip3 install azure-cognitiveservices-vision-customvision

```


How to do it

1. Create a project

Go into the Azure Portal where you created your custom vision project.

2. Create a new project.

Navigate your browser to https://customvision.ai and log in.  It will take you to the projects page.  There are some sample projects but you want to create your own.  Click on the new project tile.


Then fill out the create new project wizzard.  For this recipie we are taking pictures of food and drink items so that we can use that in awork place saftey computer vision project.  This type of computer vision could be used in an IoT shop where people are eating in an environment with contaminates such as lead such as a soder station or carcigens in 3d printer resens.  


Once you have created your project click on the cog icon in the upper right the page will have all of the keys and endpoints needed for the code in this project.  We will need that when we upload the images we captured from the last recipie.

3. Tag Images
On the main page of the project you will see a Tags button.  Click on the Untagged option and you will see all of the images you uploaded.  Click on the image and use the tools to draw a goudning box aroudn the images.

tags.png

From here you can draw bounding boxes around your images and tag them.

beverage.png

4. Training the model
From here you can click on the green train button and train the model.

Train.jph

5. Getting the keys
After you click on train.  It will start to train a model.  This could take quite some time.  After it completes click on the iteration and then click on the prediciton url button. 

predict.jpg

This will give you a window with everything you need to send an image to the object detection service.

6. Testing the model

import requests

file = open('images/drink1/cap0.jpg', 'rb')
url = 'Your iteration url goes here'
headers = {'Prediction-Key': 'key from the prediction url', 'Content-Type':'application/octet-stream'}
files = {'file': file}
r = requests.post(url,  data=file, headers=headers)
json_data = r.json()
print(json_data)

How it works
Cognitive Services uses the tagged images to create a model that finds those images within a larger picture.  As the number of images grow so does the accuracy.  There will be a point where, however the accuracy reaches convergance or in laymans terms does not improve.  To find this convergance add and tag more images untill the iteration metrics of precision, recall, and mAP do not improve.

Accuracy.jpg




Using Transfer Learning for Object Detection

Real-time object detection on GPU enabled devices with Yolo

Classifying Images on constrained devices with HAAR Cascade


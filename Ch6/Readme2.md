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

1. Get your keys

Go into the Azure Portal where you created your custom vision project and grab the key and endpoint from the keys blade in the portal. Save these for later.

2. Create a new project.

Navigate your browser to https://customvision.ai and log in.  It will take you to the projects page.  There are some sample projects but you want to create your own.  Click on the new project tile.

Newproject.png

Then fill out the create new project wizzard.  For this recipie we are taking pictures of food and drink items so that we can use that in awork place saftey computer vision project.  This type of computer vision could be used in an IoT shop where people are eating in an environment with contaminates such as lead such as a soder station or carcigens in 3d printer resens.  

createnweproejct.png


Once you have created your project click on the cog icon in the upper right and copy down the project id.  We will need that when we upload the images we captured from the last recipie.

3. 

Using Transfer Learning for Object Detection

Real-time object detection on GPU enabled devices with Yolo

Classifying Images on constrained devices with HAAR Cascade


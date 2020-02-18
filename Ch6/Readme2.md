Using Microsoft’s Custom vision to label your images.
Microsofts Cognitive Services offer a one-stop-shop for everything you need for training images and deploying models.  First it provides a way of uploading images.  Then it has a UI for drawing bounding boxes around images, finally it allows you to deploy and exposes an API endpoint you can use for classifiying your images.  

Getting started
To use the Microsoft's custom vision service you will need an Azure subscription.  Then you will need to spin up a new custom vision project.  There is a free tier for testing out small models and a paid tier for larger models and serving models at scale.  After creating the Custom Vision project in the Azure portal you will see 2 new project in the resource group.  The first will be for training and the second will have a "-prediction" appended to the name which will be used for the predictions.  You will then need to go into both services and and get the service key and API endpointa from keys tab in the portal. 

Then you will need images of what you are classifying. In our case we are idenfying beverages in an environment with led and carcigin exposre. If you have completed the last recipie you will have a capturing images at one second intervals.  To make an object dection model in Cognitive Services you will need at least 30 images of each thing you are trying to classify.  More images will improve accuracy. To get good accuracy you should very the light, background, angle, size, type, and indvidual and grouped images of the objects.






Using Transfer Learning for Object Detection

Real-time object detection on GPU enabled devices with Yolo

Classifying Images on constrained devices with HAAR Cascade


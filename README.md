# Artificial Intelligence for IoT Cookbook

<a href="https://www.packtpub.com/product/artificial-intelligence-for-iot-cookbook/9781838981983?utm_source=github&utm_medium=repository&utm_campaign=9781800208919"><img src="https://static.packt-cdn.com/products/9781838981983/cover/smaller" alt="Learn Amazon SageMaker" height="256px" align="right"></a>

This is the code repository for [Artificial Intelligence for IoT Cookbook](https://www.packtpub.com/product/artificial-intelligence-for-iot-cookbook/9781838981983?utm_source=github&utm_medium=repository&utm_campaign=9781838981983), published by Packt.

**Over 70 recipes for building AI solutions for smart homes, industrial IoT, and smart cities**

## What is this book about?
Artificial intelligence (AI) is rapidly finding practical applications across a wide variety of industry verticals, and the Internet of Things (IoT) is one of them. Developers are looking for ways to make IoT devices smarter and to make users’ lives easier. With this AI cookbook, you’ll be able to implement smart analytics using IoT data to gain insights, predict outcomes, and make informed decisions, along with covering advanced AI techniques that facilitate analytics and learning in various IoT applications. Using a recipe-based approach, the book will take you through essential processes such as data collection, data analysis, modeling, statistics and monitoring, and deployment. 

You’ll use real-life datasets from smart homes, industrial IoT, and smart devices to train and evaluate simple to complex models and make predictions using trained models. Later chapters will take you through the key challenges faced while implementing machine learning, deep learning, and other AI techniques, such as natural language processing (NLP), computer vision, and embedded machine learning for building smart IoT systems. In addition to this, you’ll learn how to deploy models and improve their performance with ease.

By the end of this book, you’ll be able to package and deploy end-to-end AI apps and apply best practice solutions to common IoT problems

This book covers the following exciting features: 
* Explore various AI techniques to build smart IoT solutions from scratch
* Use machine learning and deep learning techniques to build smart voice recognition and facial detection systems
* Gain insights into IoT data using algorithms and implement them in projects
* Perform anomaly detection for time series data and other types of IoT data
* Implement embedded systems learning techniques for machine learning on small devices
* Apply pre-trained machine learning models to an edge device
* Deploy machine learning models to web apps and mobile using TensorFlow.js and Java

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1838981985) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from torch.utils.data.sampler import SubsetRandomSampler

```

**Following is what you need for this book:**
If you’re an IoT practitioner looking to incorporate AI techniques to build smart IoT solutions without having to trawl through a lot of AI theory, this AI IoT book is for you. Data scientists and AI developers who want to build IoT-focused AI solutions will also find this book useful. Knowledge of the Python programming language and basic IoT concepts is required to grasp the concepts covered in this artificial intelligence book more effectively.

Readers should have a basic understanding of software development. This book uses the Python, C, Java languages. A basic understanding of how to install libraries and packages in these languages as well as basic coding concepts such as arrays and loops will be helpful. A few websites that can help you brush up on the basics of different languages are:

* [https://www.learnpython.org/](https://www.learnpython.org/)
* [https://www.learnjavaonline.org/](https://www.learnjavaonline.org/)
* [https://www.learn-c.org/](https://www.learn-c.org/)

To get the most out of this book a basic understanding of machine learning principles will be beneficial. The hardware used in this book are off the shelf sensors and common IoT development kits and can be purchased from sites such as Adafruit.com and Amazon.com. Most of the code is portable across devices. Device code written in Python can be easily ported to a variety of microprocessors such as a Raspberry Pi, Nvidia Jetson, Lotte Panda, or sometimes even a PC. While code written in C can be ported to a variety of microcontrollers such as the ESP32, ESP8266, and Arduino. Code written in Java can be ported to any android device such as a tablet or phone.

This book uses Databricks for some of the experiments. Databricks has a free version [here](https://community.cloud.databricks.com).

With the following software and hardware list you can run all code files present in the book (Chapter 1-9).

### Software and Hardware List

| Chapter  | Hardware / Software required                                                         | OS required                        |
| -------- | -------------------------------------------------------------------------------------| -----------------------------------|
| 1 - 9    |  Raspberry Pi, ESP32, ESP8266, Nvidia Jetson, Lotte Panda                     				| Windows, Mac OS X, and Linux (Any) |
|          |  Databricks                                                                          |                                    |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781838981983_ColorImages.pdf).

### Related products <Other books you may enjoy>
* Artificial Intelligence with Python Cookbook [[Packt]](https://www.packtpub.com/product/artificial-intelligence-with-python-cookbook/9781789133967) [[Amazon]](https://www.amazon.com/dp/1789133963)

* Hands-On Artificial Intelligence for Banking [[Packt]](https://www.packtpub.com/product/hands-on-artificial-intelligence-for-banking/9781788830782) [[Amazon]](https://www.amazon.com/dp/1788830784)

## Get to Know the Author
**Michael Roshak** is a cloud architect and strategist with extensive subject matter expertise in enterprise cloud transformation programs and infrastructure modernization through designing, and deploying cloud-oriented solutions and architectures. He is responsible for providing strategic advisory for cloud adoption, consultative technical sales, and driving broad cloud services consumption with highly strategic accounts across multiple industries.	



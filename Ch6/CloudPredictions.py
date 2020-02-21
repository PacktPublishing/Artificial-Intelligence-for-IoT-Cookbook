#!venv/bin/python
import requests

file = open('images/drink1/cap0.jpg', 'rb')
url = 'https://aibenchtest.cognitiveservices.azure.com/customvision/v3.0/Prediction/6ea65006-0a20-4518-b916-7eca7f1f197e/detect/iterations/Iteration1/image'
headers = {'Prediction-Key': '9c5da3f162c04c45b85be1eb5c2ca33b', 'Content-Type':'application/octet-stream'}
#payload = {'client_id': 1}
files = {'file': file}
r = requests.post(url,  data=file, headers=headers)
json_data = r.json()
print(json_data)
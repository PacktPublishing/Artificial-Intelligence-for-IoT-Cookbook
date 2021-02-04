#!venv/bin/python
import requests

file = open('images/drink1/cap0.jpg', 'rb')
url = ''
headers = {'Prediction-Key': '', 'Content-Type':'application/octet-stream'}
#payload = {'client_id': 1}
files = {'file': file}
r = requests.post(url,  data=file, headers=headers)
json_data = r.json()
print(json_data)
import requests
import json
from playsound import playsound

auth = 'EndpointKey '
question = 'how many calories in a cheese burger'
projectURL = ''

headers = {
    'Authorization': auth,
    'Content-type': 'application/json',
}

data = '{ "question":"'+question+'"}'

response = requests.post(projectURL, headers=headers, data=data)
json_data = json.loads(response.text)

for meta in json_data['answers'][0]['metadata']:
    if meta['name'] == "file":
        audiofile = 'audio/' + meta['value']
        print(audiofile)
        playsound(audiofile)

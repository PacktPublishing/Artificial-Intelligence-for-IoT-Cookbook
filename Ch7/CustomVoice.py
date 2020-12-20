import requests
from playsound import playsound

Endpoint_key = ''
location = ''
deploymentid = '' 
project_name = 'Mikes Demo'
text = "Hey, this is mikes demo"
def get_token():
        fetch_token_url = f"https://{location}.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
            'Ocp-Apim-Subscription-Key': Endpoint_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        access_token = str(response.text)
        return access_token

constructed_url = f"https://{location}.voice.speech.microsoft.com/cognitiveservices/v1?deploymentId={deploymentid}"
headers = {
    'Authorization': 'Bearer ' + get_token(),
    'Content-Type': 'application/ssml+xml',
    'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
    'User-Agent': project_name 
}

body = f"""<speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xml:lang=\"en-US\">
<voice name=\"Siraj\">{text}</voice></speak>"""   

response = requests.post(constructed_url, headers=headers, data=body)
if response.status_code == 200:
    with open('sample.wav', 'wb') as audio:
        audio.write(response.content)
        playsound('sample.wav')
        print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
else:
    print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
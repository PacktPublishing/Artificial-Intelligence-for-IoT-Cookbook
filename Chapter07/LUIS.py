import requests

text_query = "a vanilla milk shake would be lovely"
r = requests.get(f'URL YOU COPIED &query={text_query}')
message = r.json()

print(message['prediction']['topIntent'])
for entity in message['prediction']["entities"]['$instance']:
    print(entity)


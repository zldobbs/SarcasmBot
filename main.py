import json
import requests
from bottle import route, run, template 

config = json.load(open('config.json', 'r'))

# print(config['bot_id'])

# requests.post('https://api.groupme.com/v3/bots/post', data = { 
#     "text": "fucking shit tyler I don't know man I'm so sad", 
#     "bot_id": config['bot_id']
# })

@route('/bot_message') 
def handle_message():
    print request
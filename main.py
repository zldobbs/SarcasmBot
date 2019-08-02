from flask import Flask, request
import requests
app = Flask(__name__)

# Should be imported from a config file to be secure.. but this is just quick, dirty fun
BOT_ID = "###"
BOT_NAME = "."

def send_bot_msg(msg):
    fun_msg = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(msg))
    print('Sending: ' + fun_msg)
    requests.post('https://api.groupme.com/v3/bots/post', data = {"text": fun_msg, "bot_id": BOT_ID})
    return

@app.route('/')
def hello_world():
    return 'You are doing great sweetie'

@app.route('/bot_msg', methods=['POST'])
def handle_bot_msg():
    data = request.get_json()
    print(data)
    if (data['name'] != BOT_NAME) and (data['text'][0] == '#'):
        print(data['text'])
        send_bot_msg(data['text'][1:])
    return 'Someone sent a message'
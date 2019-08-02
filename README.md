# SaRcAsM BoT

![Not a Spongebob Meme](https://ww2.kqed.org/pop/wp-content/uploads/sites/12/2018/11/mockingspongebobbb-800x450.jpg "Not a Spongebob Meme")

A fun little python API for GroupMe chats. Will replace any message sent with a hashtag with a sarcastic rendition. 
For example: 

#why did you make this? 

gets translated to:

WhY dId YoU mAkE tHiS?

Feel free to use it in your own GroupMe chats:

Note: This is built with [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- First, create a GroupMe bot on the [GroupMe developers portal](https://dev.groupme.com)
- Next, copy the bot ID into the BOT_ID field of main.py 
- Finally, host your script and set the bot's callback to point to <your_site>/bot_msg 

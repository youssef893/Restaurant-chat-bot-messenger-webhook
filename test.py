import requests

request = requests.post('https://youssefchatbot.herokuapp.com/webhooks/rest/webhook', json={"message": "youssef sayed ahmed"})

print("Bot says, ", end='')
bot_message = ''
for i in request.json():
	bot_message = i['text']
	print(f"{bot_message}")
import requests

request = requests.post('https://youssefchatbot.herokuapp.com/webhooks/rest/webhook', json={"message": "hello"})

print("Bot says, ", end='')
bot_message = ''
print(request.json())
for i in request.json():
	bot_message = i['text']
	print(f"{bot_message}")
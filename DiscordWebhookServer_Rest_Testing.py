import os
import requests

# Discord Webhook URL
webhook_url = os.getenv('DISCORD_URL')

message = 'Hello, Discord! This is a test message Testing YAAAAAA.'

data = {
    'content': message
}

response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print('Message sent successfully!')
else:
    print('Failed to send message.')

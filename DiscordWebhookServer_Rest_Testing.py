import os
import requests

# Discord Webhook URL
webhook_url = os.getenv('DISCORD_URL')
# 要发送的消息内容
message = 'Hello, Discord! This is a test message Testing YAAAAAA.'

# 构建消息数据
data = {
    'content': message
}

# 发送 HTTP POST 请求到 Discord Webhook
response = requests.post(webhook_url, json=data)

# 检查响应状态码
if response.status_code == 204:
    print('Message sent successfully!')
else:
    print('Failed to send message.')

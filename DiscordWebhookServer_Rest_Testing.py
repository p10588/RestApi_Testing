import requests

# Discord Webhook URL
webhook_url = 'https://discord.com/api/webhooks/1149263328003227669/b5MFz_VJ8y9YXAguieMziRoz5xXok8VIcOyNp8DrmbGXrqEOMIUu1b327ldBR744suPD'

# 要发送的消息内容
message = 'Hello, Discord! This is a test message.'

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

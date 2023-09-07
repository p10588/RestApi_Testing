import os
import requests

api_key = os.getenv('OPENAI_API_KEY')

url = 'https://api.openai.com/v1/chat/completions' # 定义要发送的数据

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Hello!'}
    ],
    'temperature': 0.7
   }

# 定义要发送的标头
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}


response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    data = response.json()
    print("API Response:", data)
else:
    print("API Request Failed with Status Code:", response.status_code)

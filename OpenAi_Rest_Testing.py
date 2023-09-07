import os
import requests

api_key = os.getenv('OPENAI_API_KEY')

url = 'https://api.openai.com/v1/chat/completions' # 定义要发送的数据

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'system', 'content': '你是一個浪漫的戀人.'},
        {'role': 'user', 'content': '我心情不好'}
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
    print("API Response:", data['choices'][0]['message']['content'])
else:
    print("API Request Failed with Status Code:", response.status_code)

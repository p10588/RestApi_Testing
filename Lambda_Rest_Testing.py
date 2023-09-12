import os
import requests

url = os.getenv('LAMBDA_TEST_URL')

data = {
    'model': 'gpt-3.5-turbo',
   }

# 定义要发送的标头
headers = {
    'Content-Type': 'application/json'
    # 'Authorization': f'Bearer {api_key}',
}


response = requests.post(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("API Response:", data)
    chat("https://api.openai.com/v1/chat/completions" )
else:
    print("API Request Failed with Status Code:", response.status_code)
    print(response.content)


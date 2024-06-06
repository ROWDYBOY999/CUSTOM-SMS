import json
import requests

number = input("Enter the number: ")
msg = input("Enter the message: ")

url = f'https://peakywebapp.sbs/sms/?msg={msg}&number={number}'

response = requests.get(url)
code = response.status_code

response_data = {
    'telegram': '@rowdyboyx',
    'status': {
        'code': code,
        'api_resp': response.json()
    }
}

print(json.dumps(response_data, indent=4))

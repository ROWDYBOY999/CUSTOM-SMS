import json
import requests

number = input("Enter the number: ")
msg = input("Enter the message: ")

url = f'https://shopapp.self-shopping.com/public/selfapi/?sendnumberverifyotp=1&random=0.9304616635066649&contact={number}&otp={msg}'

response = requests.get(url)
code = response.status_code

response_data = {
    'telegram': '@TeamNoob_Official',
    'status': {
        'code': code,
        'api_resp': response.json()
    }
}

print(json.dumps(response_data, indent=4))

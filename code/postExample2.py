import requests

url = 'https://64dd7529825d19d9bfb12c36.mockapi.io/order'

user_data = {
    "name": "Pedro Otávio Alcantra",
    "order": "4554",
    "email": "pedro@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
  
    print(response.status_code)
    print(response.reason)
  
    print(response.json())
   
else:
    
    print(response.status_code)
    print(response.reason)
    print(response.text)
   
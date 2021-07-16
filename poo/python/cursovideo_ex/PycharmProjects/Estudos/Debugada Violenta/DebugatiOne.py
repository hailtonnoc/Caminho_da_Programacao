import requests
url = 'https://api.exchangerate-api.com/v6/latest'
req= requests.get(url)

print(req.status_code)

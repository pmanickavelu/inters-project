import requests

url = "http://www.amazon.in/Xbox-One-1TB-Console-Division/dp/B01F6WX6LQ"

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

response.text

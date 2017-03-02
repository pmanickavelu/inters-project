import requests
from bs4 import BeautifulSoup
url = "http://www.amazon.in/Xbox-One-1TB-Console-Division/dp/B01F6WX6LQ"

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

response.text
soup = BeautifulSoup(response.text, 'html.parser')
print soup.find(id= "priceblock_ourprice")
print soup.find(id="productTitle")
print soup.find(id="wayfinding-breadcrumbs_feature_div").find_all("a", class_=["a-link-normal","a-color-tertiary"])

import urllib2
from bs4 import BeautifulSoup
response = urllib2.urlopen('http://www.amazon.in/Xbox-One-1TB-Console-Division/dp/B01F6WX6LQ')
html = response.read()
print html
# soup = BeautifulSoup(html, 'html.parser')
# print soup
# print soup.find_all("div",class_="_3eAQiD")
# print soup.div

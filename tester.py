# this is a playground codes here not supossed to work or look pretty 

import requests
from bs4 import BeautifulSoup



base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

for text in soup.find_all(class_="content-section"):
    print(text.get_text())

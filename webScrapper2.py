#packages
from bs4 import BeautifulSoup
import requests

# user input
fileName = input('how should we name your file: ')

## requesting
url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'

c = []

r = requests.get(url)
# extract all the text from the page
soup = BeautifulSoup(r.text, 'html.parser')

for i in soup.findAll(class_="section"):
   # print(i.text.replace("\n", " ").strip())
   
    c.append(i.text.replace("\n", " ").strip())
    
s = ''.join(c)



# make a file and write on it
with open(f'{fileName}.txt', 'w') as open_file:
    open_file.write(s)
d
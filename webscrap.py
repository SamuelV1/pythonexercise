#packages
from bs4 import BeautifulSoup
import requests

## requesting
url = 'http://www.nytimes.com'
#
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
## get each headline and a
for story_wrapper in soup.find_all(class_="story-wrapper"): 
    if story_wrapper.a: 
        #removing the spaces and default formatation that the beautisoup give us
        print(story_wrapper.a.text.replace("\n", " ").strip())
    else: 
        print(story_wrapper.contents[0].strip())



#challenge 30
from random import randint
import random


def wordpicker():
    with open('listofwords.txt', 'r') as f:
        wordpool = [word for word in f]
    print(random.choice(wordpool))

wordpicker()
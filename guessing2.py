"""
the original challenge wanted the bot to guess between 1-100 but it would be too boring 
since their answer would go each number a time so i reduced it to 1-20 and made the bot
pick a random value this way it seems like the bot is really trying to guess and not just
spiting numbers 
"""
from random import randint
import random

playing = True 
guess = random.randint(1,20)

while playing:
    print("Is it %s?" % str(guess))
    game = int(input("1-YES 2-NO: "))
    if game == 1:
        print("THANKS FOR PLAYING")
        playing = False
    else:
        user_hint = int(input("1-higher and 2-lower: "))
        if user_hint == 1:
          guess = random.randint(guess,20)
        elif user_hint == 2:
                guess = random.randint(1,guess)
import random
from random import randint


#re using code from wordpicker

with open('listofwords.txt', 'r') as f:
    wordpool = [word for word in f]
word = random.choice(wordpool)
    
playing = True
chances = 0
placeholder = []
hangmanpics = ['''
+---+
| |
|
|
|
|
=========''', '''
+---+
| |
O |
|
|
|
=========''', '''
+---+
| |
O |
| |
|
|
=========''', '''
+---+
| |
O |
/| |
|
|
=========''', '''
+---+
| |
O |
/|\ |
|
|
=========''', '''
+---+
| |
O |
/|\ |
/ |
|
=========''', '''
+---+
| |
O |
/|\ |
/ \ |
|
=========''']

for i in range(len(word)):
    placeholder.append("_")

print("WELCOME TO HANGMAN")
while playing:
    print("pick a letter")
    print(*placeholder)
    user_guess = input("enter your letter: ")
    if user_guess in word:
        indices = [i for i, x in enumerate(word) if x == user_guess]
        #using slicing to replace the word
        for i in range(len(indices)):
            placeholder = placeholder[:indices[i]]+[user_guess]+placeholder[indices[i]+1:]
        #checks if the user already guessed the whole word
        if "".join(placeholder) == word:
            print("CONGRATULATION")
            print("thanks for playing")
            playing = False
    else:
        if chances >= 6:
            playing = False
            print(" ")
            print(" ")
            print("YOU FAILED")
            print(f"the word was: {word}")
        print(hangmanpics[chances])
        chances += 1
        
        
        
        
        


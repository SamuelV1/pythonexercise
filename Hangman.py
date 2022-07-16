word = "evaporate"
# problema o .index so pega o primeiro index o jogo não funciona em palavras com a mesma letra 2 vezes
playing = True

placeholder = []

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
        
        


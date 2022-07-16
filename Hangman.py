word = "eva"
# ideais eu posso criar uma lista de _ do tamanho da palavra ai eu pego o index da letra e mudo o _ para a letra
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
        user_guess_index = word.index(user_guess)
        #using slicing to replace the word
        placeholder = placeholder[:user_guess_index]+[user_guess]+placeholder[user_guess_index+1:]
        #checks if the user already guessed the whole word
        if "".join(placeholder) == word:
            print("CONGRATULATION")
            print("thanks for playing")
            playing = False
        
        


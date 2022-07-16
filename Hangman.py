word = "evaporate"
# ideais eu posso criar uma lista de _ do tamanho da palavra ai eu pego o index da letra e mudo o _ para a letra
playing = True

placeholder = []

for i in range(len(word)):
    placeholder.append("_")

print(*placeholder)
while playing:
    print("pick a letter")
    user_guess = input("enter your letter: ")
    if user_guess in word:
        print("ta porra menor")
        playing = False


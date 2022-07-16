# this is a playground codes here ARE NOT supossed to work or look pretty 
word = "EVA"
word2 = ["E","V", "A"]
placeholder = []
c = len(word)
print(c)

print(word[1])

for i in range(c):
    placeholder.append("_")
new_word = "".join(word2)
print(new_word)
print(*placeholder)

if word == new_word:
    print("ok sim")
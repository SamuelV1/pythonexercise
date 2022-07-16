# this is a playground codes here ARE NOT supossed to work or look pretty 
word = "EVARE"
word2 = ["E","V","A","R","E",]
placeholder = []
c = len(word)
print(c)
print(*placeholder)
print(word[1])



for i in range(c):
    placeholder.append("_")
new_word = "".join(word2)

for i in range(len(indices)):
    placeholder = placeholder[:indices[i]]+["E"]+placeholder[indices[i]+1:]
print(new_word)
print(*placeholder)

if word == new_word:
    print("ok sim")
    
print(indices)
import json
from collections import Counter

with open("info.json", "r") as f:
    info = json.load(f)

c = []

for k in info.keys():
    birthday = info[k].split()
    c.append(birthday[0])


result = Counter(c)
print(result)
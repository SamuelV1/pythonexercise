import json

with open("info.json", "r") as f:
    info = json.load(f)


c = info.keys()

print(*c, sep = ', ')

user_new_person = str(input("Who birthday you wanna add to the dictionary: "))
user_newP_data = str(input("and when is this person birthday: "))

info[user_new_person] = user_newP_data

print(info)

with open("info.json", "w") as f:
    json.dump(info, f)
    
print("your data been saved :) ")
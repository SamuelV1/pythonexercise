bday_dict = {
"James Hetfield": "August 3rd, 1963",
"Kirk Hammett": "November 18, 1962",
"Lars": "December 26, 1963",
"Cliff Burton": "February 10, 1962"
}

c = bday_dict.keys()

print(*c, sep = ', ')

user_input = str(input("who birthday u wanna know: "))

if user_input in c:
    print(bday_dict[user_input])
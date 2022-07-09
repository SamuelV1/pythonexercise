
from random import randint
# futuro: adicionar um loop while que so quebrar se o usuario me der um numero de 4 digitos 

print("Cows and Bulls game guest the computer exact number")
print("  ")
#get user 4 guess
user_guess = int(input("pick a four number digit: "))

#game variable
bulls = 0
cows = 0

#edited previously used function
def random4digits():
    range_start = 10**(4-1)
    range_end = (10**4)-1
    return randint(range_start, range_end)

computer_guess = random4digits()

computer_list = [int(i) for i in str(computer_guess)]
user_list = [int(i) for i in str(user_guess)]

for i in range(len(computer_list)):
    if computer_list[i] == user_list[i]:
        cows += 1
    elif user_list[i] in computer_list:
        bulls += 1

print(f"you got {cows} cows and {bulls} bulls")
print("   ")
print(f"the computer number was: {computer_guess}")
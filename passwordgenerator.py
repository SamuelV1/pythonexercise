import random
import string
from random import randint

## random punctuation
def random_punctuation(y):
       return ''.join(random.choice(string.punctuation) for x in range(y))
#function to get a especif number of random letters
def random_char(y):
       return ''.join(random.choice(string.ascii_lowercase) for x in range(y))
       
def random_charup(y):
       return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
       
# function to get random digit of numbers
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
    

# print(b+d+a+str(c))


## now function
passwordLevel = int(input("password generator 1 for simple 2 for extra strong: "))

print(passwordLevel)
#if the password is weak it will only have number and lowercase letters
if passwordLevel == 1:
    weak_leeter = random_char(random.randint(3,6)) 
    weak_numbers = random_with_N_digits(random.randint(3,5))    
    print (f"Here is your new password: {weak_leeter+str(weak_numbers)}")
    #output example: pfloz2558
    
    #if the password is stronger it will have everything possible
elif passwordLevel == 2:
    
    a = random_charup(random.randint(2,4))
    b = random_punctuation(random.randint(3,4))
    c = random_char(random.randint(1,4)) 
    d = random_with_N_digits(random.randint(3,5))
    print(f"Here is your newpassword: {c+b+a+str(d)}")
    #example output: m.]]^WYQT6317
    #Time to crack this password:
    #  10 billion years
    

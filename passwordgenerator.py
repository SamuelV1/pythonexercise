import random
import string
from random import randint
#stash of letter
LowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase


## random punctuation
def random_punctuation(y):
       return ''.join(random.choice(string.punctuation) for x in range(y))
#function to get a especif number of random letters
def random_char(y):
       return ''.join(random.choice(string.ascii_lowercase) for x in range(y))
def random_charup(y):
       return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
       
d = random_charup(random.randint(1,5))
a = random_punctuation(random.randint(1,5))

b = random_char(random.randint(1,6)) 
# function to get random digit of numbers
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
    
c = random_with_N_digits(random.randint(1,5))
# print(b+d+a+str(c))


## now function
passwordLevel = int(input("password generator 1 for weak 2 for extra strong: "))

print(passwordLevel)

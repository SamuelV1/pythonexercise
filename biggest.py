# since we cant use .max()

def biggest(n1, n2, n3):
    c = []
    c.extend([n1,n2,n3])
   
    big = c[0]
    for number in c:
        if number > big:
            big = number
    #returns the biggest number in this case 9
    print(big)
    
biggest(2,8,9)
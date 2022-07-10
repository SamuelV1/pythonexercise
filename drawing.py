x = " --- "
y = "|   " 

def boardPrinter(size):
    for index in range(size):
        print(x * size)
        print(y *(size + 1))

boardPrinter(2)
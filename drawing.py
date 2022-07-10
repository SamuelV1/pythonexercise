x = " --- "
y = "|   " 

def boardPrinter(size):
        print(size*(size*x+'\n'+(size+1)*y+'\n')+size*x)

boardPrinter(4)
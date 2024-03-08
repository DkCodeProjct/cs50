import random


def main():
    problem = 5
    attmpt = 3
    level = int(input('Level: '))
    getOp = int(input('1-,2+,3*,4/'))
    for _ in range(problem):
        x,y = generate_integer(level)
        
        
        for _ in range(attmpt):
            if getOp == 1:
                sign = '-'
                op = x-y
            elif getOp == 2:
                sign = '+'
                op = x+y

            elif getOp == 3:
                sign = '*'
                op = x*y
            else:
                sign = '/'
                op = x/y
            ask = int(input(f'{x}{sign}{y} '))
            if ask == op:
                print('correct')
               
                break
            else:
                print()
            

def get_level(level):
    while True:
        try:
            get = int(input(level))
            if get in [1,2,3]:
                return get 
            else:
                pass
        except ValueError:
            pass
    
def generate_integer(level):
    if level == 1:
        x = random.randint(1,10)
        y = random.randint(1,10)
    elif level == 2:
        x = random.randint(10,100)
        y = random.randint(10,100)
    else:
        x = random.randint(100,1000)
        y = random.randint(100,1000)
    return x, y
    

if __name__ == "__main__":
    main()
         
        
                

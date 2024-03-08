import random


def main():
    problem = 10
    attmpt = 3
    score = 0
    
    level = get_level()
    
    for _ in range(problem):
        x,y = generate_integer(level)
        for _ in range(attmpt):
            try:
                ask = int(input(f'{x} + {y} = '))
                if ask == x+y:
                    problem-=1
                    score += 1
                    break
                
                else:
                    print('EEE')
            
            except ValueError:
                print("EEE")
                pass
        
        if ask != x+y: 
            print(f'Correct answer: {x} + {y} = {x+y}')
            
    
    print(f'Score = 10/{score}')
               
            
        
    
            

def get_level():
    while True:
        try:
            get = int(input('Level:'))
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
        
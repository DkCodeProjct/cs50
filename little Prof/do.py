import random
problem = 5
attmpts = 3
while problem != 0:
    x = random.randint(1,10)
    y = random.randint(1,10)
    
    for i in range(attmpts):
    
        ask = int(input(f"{x}+{y} "))
        if ask == x+y:
            problem -=1 
            break
        else:
            
            attmpts -=1
            continue
        
    if attmpts== 3:
        ask = int(input(f'{x}+{y} '))
        if ask == x+y:
            problem -=1 
            continue
        else:
            attmpts -=1 
            break
                



        
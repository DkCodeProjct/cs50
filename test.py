import random

attepts = 3

x = random.randint(1, 9)
y = random.randint(1, 9)

while attepts > 0:
    try:
        print(f"{x} + {y} == __")
        z = int(input("whats X "))
    except ValueError:
        pass
    
    else:
        if z == x + y:
            print("correct")
            break
        else:
            print("wrong ")
            attepts -= 1
        print()

if attepts == 0:
    print("L", x+y)
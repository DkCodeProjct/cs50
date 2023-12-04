import random
def main():
    Name = input("enter PassName: ")
    
    if passName(Name):
        
        x = random.randint(0,20)
        y = random.randint(0,20)
        attepmts = 5
        
        while attepmts>0:
            print("gussNum: num is between 0,40")
            getAns = int(input("enterNum: "))
            
            if getAns > (x+y):
                print(">thanX+Y")
                attepmts-=1
            
            elif getAns < (x+y):
                print("<thatX+Y")
                attepmts-=1
            
            else:
                print(f"correct:{x+y}...")
                print("PassKey:==[35L5m]")
                break
        
        if attepmts==0:
            print("you've reached maximum attempts")
    
    else:
        print("invlaid passName")

def passName(char):
    for c in char:
        if len(c) > 2 or len(c) < 5:
            return True
        
        if c in ["a",'e','i']:
            return False
        
        if c[4]=='@'and c[3]=="%":
            return False
if __name__ == "__main__":
    main()
        

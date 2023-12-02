import random
def main():
    getPassword = input("Enter Psswrd[#,#,#,#]\npsswrd: ")
    
    if isvalid(getPassword):
        getName = input("name: ")
        if isVerified(getName):
            print("Welcome TO the numGuess Game")
            attepts = 3
            for i in range(3):
                while attepts > 0:
                    x = random.randint(0,9) 
                    y = random.randint(0,9) 
                    
                    print("whats x")
                    getAnswer = int(input(f"{x}+{y} == "))
                    
                    if getAnswer == (x+y):
                        print("Correct")
                        break
                    else:
                        print("invalid")
                        attepts -= 1
                if attepts == 0:
                    print("loose")
        else:
            print("invlaidName")
    else:
        print("invalidPassword")

def isvalid(n):
    x,y,z,i = n.split(",")
    newx = int(x)
    newy = int(y)
    newz = int(z)
    newi = int(i)
    if newx + newy + newz + newi == 23:
        return True
    else:
        return False

def isVerified(s):
    if len(s) > 0 and len(s) < 5:
        return True
    if s[0].isalpha() == False and s[1].isalpha() == False:
        return False
    if s[2].isupper() == False or s[3].isupper() == False:
        return False
    if s[4] == "@":
        return True

if __name__ == '__main__':
    main()
    

    
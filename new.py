import random

def main():
    level = getLevel()
    score = simulateGame(level)
    print(f"score:_ 5/{score}")

def getLevel():
    while True:
      try:
         level = int(input("choose level[1/2/3] "))
      except ValueError:
         pass
      
      else:
         if level in [1, 2, 3]:
            return level
         else:
            print("level was not in [1/2/3]")

def genNum(level):
   
   if level == 1:
      x = random.randint(0, 9)
      y = random.randint(0, 9)
  
   elif level == 2:
      x = random.randint(9, 99)
      y = random.randint(9, 99)
   
   else:
      x = random.randint(99, 999)
      y = random.randint(99, 999)
   
   return x, y

def simulateRound(x, y):
   tries = 3
   while tries > 0:
      try:
         getUsreAnswer = int(input(f"{x}+{y}= "))
      except ValueError:
         pass
      else:
         
         if getUsreAnswer == (x+y):
            return True
         else:
            print("EEE")
            tries -= 1
   
   print(f"{x}+{y}= {x+y} ")

def simulateGame(level):
   score = 0
   for i in range(5):
      
      x,y = genNum(level)
      if simulateRound(x,y):
         
         print("correct")
         score += 1
      
      else:
         print("EEE")
   return score

if __name__ == "__main__":
   main()
      


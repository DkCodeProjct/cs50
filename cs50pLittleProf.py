import random

#
#   Solve This After finish cs50, its been 3 months i guess, quit good skills  
# 
#
class LittleProf:
    def __init__(self):
        self.quiz = 10
        self.attempt = 3
        self.score = 0
        

    def littleProf(self):
        level = self.getLevel()
        for i in range(self.quiz):
            x, y = self.genNum(level)
            for i in range(self.attempt):
                quiz = int(input(f'{x} + {y} == '))
                if quiz == x + y:
                    print('Correct')
                    self.score += 1
                    break
                else:
                    print('EEE')
                    quiz = quiz
                    if quiz == x + y:
                        self.score += 1
                        break
                    continue
        print(f'Score:{self.score}')

        
    def getLevel(self):
        while True:
            try:
                get = int(input("> choose Level: "))
                if get not in [1,2,3]:
                    print('not in [1,2,3]')
                return get
            except ValueError:
                pass
    
    def genNum(self, level):
        if level == 1:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
        elif level == 2:
            x = random.randint(10, 100)
            y = random.randint(10, 100)
        else:
            x = random.randint(100, 1000)
            y = random.randint(100, 1000)
        return x, y

lp = LittleProf()
lp.littleProf()
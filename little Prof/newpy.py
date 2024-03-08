import random

x = random.randint(1,10)
y = random.randint(1,10)
getOp = int(input('1-,2+'))
if getOp == 1:
    sign = '-'
    op = x-y
else:
    sign = '+'
    op = x+y
ask = int(input(f'{x}{sign}{y} = op'))

if ask == op:
    print('correct')
else:
        print("ww")
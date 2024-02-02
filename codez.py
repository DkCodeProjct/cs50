import inflect

####-----> Learn how to read docs <-----####
#put  .. instead EOFEror work as expected

p = inflect.engine()
c = []
while True:
    
    getname = input('names ')
    c.append(getname)
    if getname == '..':
        print()
        break 
outPut = p.join(c)
print(outPut)


"""
#work as exceptet BUT if EORError works correctly it didnt getting ^d
import inflect

p = inflect.engine()
c = []

while True:
    try:
        names = input('name: ')
        c.append(names)
    except EOFError():
        print()
        break
outPut= p.join(c)
print('Adiue adiue to', outPut)

""" 

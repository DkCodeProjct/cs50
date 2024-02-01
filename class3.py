from pyfiglet import Figlet
import pyfiglet
import random
import sys

if (len(sys.argv) == 1):
    
    getFont = input('Input: ')
    fonts = pyfiglet.FigletFont.getFonts()
    random_font = random.choice(fonts)
    f = pyfiglet.Figlet(font=random_font)
    print('Output:')
    print(f.renderText(getFont))


elif (len(sys.argv) == 3 and sys.argv[1]== '--f' or sys.argv[1] == '-f' and len(sys.argv) == 3):
    
    #if font not in pyfiglet library// sys.exit()
    if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
        sys.exit('Invalid usage')
    
    getFont = input('Input: ')
    figlet = Figlet()
    figlet.setFont(font=sys.argv[2])
    print('OutPut:')
    print(figlet.renderText(getFont))

else:
    sys.exit('Invalid usage')
    


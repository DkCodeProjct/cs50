
'|' # INSTRUCTION:// https://cs50.harvard.edu/python/2022/psets/4/figlet/
'|' 
'|'  # buggy code but ive make good progress my own without help from the internet
    #only ask CS50.ai how to generate random text with the pyfiglet 



from pyfiglet import Figlet
import pyfiglet
import random
import sys

if len(sys.argv) == 1:
    
    getFont = input('Inputl: ')
    fonts = pyfiglet.FigletFont.getFonts()
    random_font = random.choice(fonts)
    f = pyfiglet.Figlet(font=random_font)
    print(f.renderText(getFont))

elif  len(sys.argv) == 3 and sys.argv[1]== '--f' or sys.argv[1] == '-f' and len(sys.argv) == 3:
    
    getFont = input('Inputl: ')
    figlet = Figlet()
    figlet.setFont(font=sys.argv[2])
    print('OutPut:')
    print(figlet.renderText(getFont))

else:
    sys.exit('ss ')
    

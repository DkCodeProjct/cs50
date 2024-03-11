import requests
import json
import sys


respns = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
o = respns.json()


if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

try:
    
    perches = float(sys.argv[1])
    
    #access the json data, go to key bpi, go to key usd  and go to ratr Value 
    rate_float = o['bpi']['USD']['rate_float']
    
    ammount = rate_float * perches  
    print(f"${ammount:,.4f}")


except (requests.RequestException, ValueError):
    sys.exit('Commant-line argument is not a number')
    
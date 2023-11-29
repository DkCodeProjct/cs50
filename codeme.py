import sys
import requests

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command Line Argument isn't INTEGER")
        sys.exit(1)
else:
    print("missing argument")
    sys.exit(1)

requestsDetails = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
response = requestsDetails.json()
bitcoinPrice = response["bpi"]["USD"]["rate_float"]
totalAmount = bitcoinPrice * value
print(f"$ {totalAmount:,.4f}")
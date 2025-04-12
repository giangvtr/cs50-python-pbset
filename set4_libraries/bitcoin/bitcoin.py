import requests
import sys


# Input for bitcoins
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
try :
    user_input = float(sys.argv[1])
    if user_input < 0:
        raise ValueError
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

# Use API
try :
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    result = float(data["bpi"]["USD"]["rate_float"]) * user_input
    print (f"${result:,.4f}")
except requests.RequestException:
    print(f"Error fetching prize :")
    sys.exit(1)

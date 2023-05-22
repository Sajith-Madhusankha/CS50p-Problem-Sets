import requests
import sys


def main():
    if len(sys.argv) == 2:
        try:
            number = float(sys.argv[1])
            print(bitcoin_price(number))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def bitcoin_price(number):
    try:
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        results = response.json()
        price = results["bpi"]["USD"]["rate_float"]
        total = price * number
        return f"${total:,.4f}"
    except requests.RequestException:
        return None


if __name__ == "__main__":
    main()
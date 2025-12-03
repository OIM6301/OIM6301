# bitcoin price api: https://data-api.coindesk.com/spot/v1/latest/tick?market=coinbase&instruments=BTC-USD


import urllib.request
import json


def get_bitcoin_price():
    """
    Fetches the current Bitcoin price in USD from the CoinDesk API.
    """
    url = "https://data-api.coindesk.com/spot/v1/latest/tick?market=coinbase&instruments=BTC-USD"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        json_data = json.loads(data)
        price = json_data["Data"]["BTC-USD"]["PRICE"]
        return price
    
def get_joke():
    """
    Fetches a random joke from the JokeAPI.
    """    
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            json_data = json.loads(data)
            if json_data["type"] == "single":
                print(json_data["joke"])
            elif json_data["type"] == "twopart":
                print(json_data["setup"])
                print(json_data["delivery"])
    except urllib.error.URLError as e:
        print(f"Error fetching data from URL: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")


def main():
    # print(get_bitcoin_price())
    get_joke()

if __name__ == "__main__":
    main()
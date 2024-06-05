'''Executes API call to get the price of a certain item; not accessed by user.'''

import requests

URL = "https://steamcommunity.com/market/priceoverview/"
# COUNTRY_CODE = "your_country_code_here" #for example US, DE, ... # Country Code is not necessary for the query.

def api_call(market_hash_name: str, currency, app_id) -> dict:
    '''Executes the API call to the steam market'''

    params = {
        #"country": COUNTRY_CODE,
        "currency": currency,
        "appid": app_id,
        "market_hash_name": market_hash_name
    }

    try:
        response = requests.get(URL, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data
        #else:
        return {"Error": f"HTTP error {response.status_code} ({response.reason}) for item: \"{market_hash_name}\""}
    except requests.exceptions.Timeout:
        return {"Error": f"Request timed out for item: \"{market_hash_name}\""}
    except requests.exceptions.RequestException as e:
        return {"Error": f"An error occured for item \"{market_hash_name}: {e}\""}

# Some currencies might not be available anymore or may not be available in your country. Below are the ones I tested with country-code "DE"

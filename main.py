'''Main file; run this'''

import json
from utils.api_caller import api_call

FILEPATH = 'utils/item_list.json'

def _price_formatter(price: str) -> float:
    '''Input: price as i.e. 39,44€ or 198,--€'''

    if "." in price:
        price = price.split(".")
    if "," in price:
        price = price.split(",")

    price0 = ""
    price1 = ""
    for char0 in price[0]:
        if char0.isdigit():
            price0 += char0
    for char1 in price[1]:
        if char1.isdigit():
            price1 += char1

    if not price1: # This means the price was only for full currency and no cents, for example 42,00€. Steam would display that as 42,--€.
        price1 = "00"

    return int(price0) + int(price1)/100

def price_calculation():
    '''Bring everything together'''
    app_id = input("Enter app ID: ")
    while True:
        currency_abbr = input("Enter the currency abbreviation you want the prices to be calculated in (i.e. EUR, USD, CHF, CNY, ...): ")
        if currency_abbr in currency_abbreviation_to_currency_code:
            break
        print("Invalid currency code! Please try again")

    with open(FILEPATH, 'r', encoding='utf-8') as file:
        print("Processing...")
        price_total = 0
        items_not_factored_in = []
        json_obj: dict = json.load(file) #returns dict
        for item_name, amount in json_obj.items():
            price_json = api_call(market_hash_name=item_name, currency=currency_abbreviation_to_currency_code[currency_abbr], app_id=app_id)
            if "Error" in price_json:
                print(price_json["Error"])
                items_not_factored_in.append(item_name)
            else:
                if 'lowest_price' in price_json:
                    price_of_item_unformatted = price_json['lowest_price']
                elif 'median_price' in price_json:
                    price_of_item_unformatted = price_json['median_price']
                else:
                    print(f"Error: Could not find price for item: {item_name}")
                    items_not_factored_in.append(item_name)
                    continue
                price_of_item = _price_formatter(price_of_item_unformatted)
                price_total += amount*(price_of_item)

        print(f"\nTotal value (before Steam fees): {price_total:.2f} {currency_abbr}")

        price_total /= 1.15
        #Steam cut of 5% + CS2 cut of 10% (for some reason it's calculated this way)

        print(f"\nTotal value (after Steam fees): {price_total:.2f} {currency_abbr}")
        if items_not_factored_in:
            print("Items not factored in due to errors:")
            for item in items_not_factored_in:
                print(item, end=";   ")
        return price_total

currency_abbreviation_to_currency_code = {
    #"USD": 0,  # Code 0 also works for United States Dollar
    "USD": 1,  # United States Dollar
    "GBP": 2,  # United Kingdom Pound
    "EUR": 3,  # European Union Euro
    "CHF": 4,  # Swiss Francs
    "RUB": 5,  # Russian Rouble
    "PLN": 6,  # Polish Złoty
    "BRL": 7,  # Brazilian Reals
    "JPY": 8,  # Japanese Yen
    "NOK": 9,  # Norwegian Krone
    "IDR": 10, # Indonesian Rupiah
    "MYR": 11, # Malaysian Ringgit
    "PHP": 12, # Philippine Peso
    "SGD": 13, # Singapore Dollar
    "THB": 14, # Thai Baht
    "VND": 15, # Vietnamese Dong
    "KRW": 16, # South Korean Won
    "TRY": 17, # Turkish Lira
    "UAH": 18, # Ukrainian Hryvnia
    "MXN": 19, # Mexican Peso
    "CAD": 20, # Canadian Dollars
    "AUD": 21, # Australian Dollars
    "NZD": 22, # New Zealand Dollar
    "CNY": 23, # Chinese Renminbi (yuan)
    "INR": 24, # Indian Rupee
    "CLP": 25, # Chilean Peso
    "PEN": 26, # Peruvian Sol
    "COP": 27, # Colombian Peso
    "ZAR": 28, # South African Rand
    "HKD": 29, # Hong Kong Dollar
    "TWD": 30, # New Taiwan Dollar
    "SAR": 31, # Saudi Riyal
    "AED": 32, # United Arab Emirates Dirham
    "SEK": 33, # Swedish Krona --- Not supported as of last test!
    "ARS": 34, # Argentine Peso
    "ILS": 35, # Israeli New Shekel
    "BYN": 36, # Belarusian Ruble --- Not supported as of last test!
    "KZT": 37, # Kazakhstani Tenge
    "KWD": 38, # Kuwaiti Dinar
    "QAR": 39, # Qatari Riyal
    "CRC": 40, # Costa Rican Colón
    "UYU": 41, # Uruguayan Peso
    "BGN": 42, # Bulgarian Lev --- Not supported as of last test!
    "HRK": 43, # Croatian Kuna --- Not supported as of last test!
    "CZK": 44, # Czech Koruna --- Not supported as of last test!
    "DKK": 45, # Danish Krone --- Not supported as of last test!
    "HUF": 46, # Hungarian Forint --- Not supported as of last test!
    "RON": 47 # Romanian Leu --- Not supported as of last test!
    # Currency codes greater than 47 will display the price in USD
}

if __name__ == '__main__':
    price_calculation()
    input("\n\nPress ENTER to close.")

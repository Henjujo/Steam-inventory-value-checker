'''This file lets you find the market hash name for all items in your inventory.'''

import requests

def inventory_call():

    steam_id = input("Copy & paste your Steam UUID: ")
    app_id = input("Enter the app ID for the game you want your items of: ")
    language = input("Enter your desired language (english, german, dutch, etc. defaults to english): ")

    url = f"https://steamcommunity.com/inventory/{steam_id}/{app_id}/2?l={language}"
    response = requests.get(url=url, params=None, timeout=10)
    json_body = response.json()
    if response.status_code == 200:
        with open(f"Market hash names for gameID={app_id}", "w", encoding="utf-8") as file:
            file.write("Item name     :     market_hash_name\n\n")
            file.write("-------------------------------------\n\n")
            try:
                for entry in json_body['descriptions']:
                    file.write(f"{entry['name']}     :     {entry['market_hash_name']}\n")
            except KeyError:
                print("Request failed. Try again please!")
    else:
        print(f"An error occured: HTTP error {response.status_code} ({response.reason})")

if __name__ == '__main__':
    inventory_call()

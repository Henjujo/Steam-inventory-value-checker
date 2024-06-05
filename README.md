# Steam Inventory value checker

This is my value calculator for your Steam inventory. I originally coded it to keep track of my CS2 cases but it's also applicable to other games.
The executables are only delivered for Windows. If you use Linux, just run the `main.py`.
Not for commercial use.

### Get market hash name values

In the `utils/item_list.json` file, you can insert the market_hash_name values of the items you want to look up.
The market_hash_name is the unique ID for each item in a game used on the steam market.
Because you may have items in CS2 storage units (like me) or similar containers, please add the amount you have of that item by yourself. Format your items the way the example is formatted.
If you do not know the market_hash_name of your item, use the `market_hash_name_finder.exe` and read the result from the created `.txt` file.
Enter your Steam UUID, the app ID (see below) and your preferred displayed language when asked.

### Get app ID

To find out the app ID of a game, go to https://steamdb.info and search for the game title. The app ID will be displayed there.
Some common IDs might be 730 (CS2) and 570 (Dota 2).


## Use the price tracker

Execute the `main.exe` file. Enter the currency you want your total money to be shown in. Available currency abbreviations are listed below.
Wait a bit and - tada! Your total money in steam items is shown.

### Available currencies:

+ USD: United States Dollar
+ GBP: United Kingdom Pound
+ EUR: European Union Euro
+ CHF: Swiss Francs
+ RUB: Russian Rouble
+ PLN: Polish Złoty
+ BRL: Brazilian Reals
+ JPY: Japanese Yen
+ NOK: Norwegian Krone
+ IDR: Indonesian Rupiah
+ MYR: Malaysian Ringgit
+ PHP: Philippine Peso
+ SGD: Singapore Dollar
+ THB: Thai Baht
+ VND: Vietnamese Dong
+ KRW: South Korean Won
+ TRY: Turkish Lira
+ UAH: Ukrainian Hryvnia
+ MXN: Mexican Peso
+ CAD: Canadian Dollars
+ AUD: Australian Dollars
+ NZD: New Zealand Dollar
+ CNY: Chinese Renminbi
+ INR: Indian Rupee
+ CLP: Chilean Peso
+ PEN: Peruvian Sol
+ COP: Colombian Peso
+ ZAR: South African Rand
+ HKD: Hong Kong Dollar
+ TWD: New Taiwan Dollar
+ SAR: Saudi Riyal
+ AED: United Arab Emirates Dirham
+ SEK: Swedish Krona
+ ARS: Argentine Peso
+ ILS: Israeli New Shekel
+ BYN: Belarusian Ruble
+ KZT: Kazakhstani Tenge
+ KWD: Kuwaiti Dinar
+ QAR: Qatari Riyal
+ CRC: Costa Rican Colón
+ UYU: Uruguayan Peso
+ BGN: Bulgarian Lev
+ HRK: Croatian Kuna
+ CZK: Czech Koruna
+ DKK: Danish Krone
+ HUF: Hungarian Forint
+ RON: Romanian Leu

### Troubleshooting

HTTP errors will be shown with their codes and a short explaination. For further information, use google. Some common ones might be:
+ Error 429 (Too many requests): You use the program too frequently. Wait for a minute and try again.
+ Error 500 (Internal server error): The market_hash_name you put into the `item_list.json` might be spelt wrong.
+ Timeout Error: Either Steam servers are down or your internet connection doesn't work/doesn't allow access to Steam servers.
+ JSON errors: https://jsonchecker.com can probably tell you whats wrong.

Those are all errors I encountered. If you find any new errors, you can probably fix them somehow. Restart your computer or something.

Feel free to reach out if you encounter any problems or have any suggestions!
Discord: henju / Henju#0351
Steam UUID: 76561198233540304
Email: henjugames2@gmail.com
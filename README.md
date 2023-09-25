# binanceVolatilityBot (Docker Ready)

## Overview
This Python-based cryptocurrency trading bot leverages the Binance API to automate the trading process. The bot's strategy is designed to identify and capitalize on short-term price movements in the cryptocurrency market. It aims to make informed buying decisions based on price volatility and predefined criteria.
## Key Features
- Pairing Currencies: The bot allows you to select the currency or fiat currency with which each cryptocurrency is paired. By default, it pairs cryptocurrencies with 'USDT' (Tether), a commonly used stablecoin.

- Trade Size: You can define the size of each trade, typically in USDT, using the QUANTITY parameter. Be cautious when changing the pairing currency, as this affects the trade size calculation.

- Excluded Pairs: The bot provides the flexibility to exclude specific currency pairs from trading. By default, it excludes popular fiat pairs and some margin keywords.

- Price Difference: The bot monitors the price difference for each cryptocurrency over a specified time period (default is 5 minutes). It considers coins that have moved by a certain percentage (default is 3%) as potential buy signals.

- Stop Loss and Take Profit: The bot includes risk management features such as stop loss and take profit percentages. If a coin's price moves beyond these thresholds, the bot will automatically sell the coin to limit losses or secure profits.

- Portfolio Tracking: The bot maintains a portfolio of coins bought during trading. It tracks essential details such as the purchase price, volume, and order ID for each coin.

## 1. Create a Virtual Environment.
   
To create a virtual environment in Python, you can use the <code>venv</code> module, which is included in Python 3.3 and later. Here's how to create a virtual environment:
- Open your command prompt or terminal.
- Navigate to the directory where you want to create the virtual environment.
  You can use the `cd` command to change directories.
  For example:
  ```bash
  cd /path/to/your/directory
  ```
 - Once you are in the desired directory, run the following command to create a virtual environment.
   You can replace <code>myenv</code> with the name you want to give your virtual environment:
   ```bash
   python3 -m venv myenv
   ```
   This command will create a directory named <code>myenv</code> (or the name you specified) in your current directory.
   Inside this directory, the virtual environment will be set up.

- To activate the virtual environment, you'll need to use the appropriate activation command based on your operating system:
  - On Windows:
  ```bash
  myenv\Scripts\activate
  ```
  - On macOS and Linux:
  ```bash
  source myenv/bin/activate
  ```
  After activation, your command prompt or terminal should indicate that you are now working within the virtual environment.

- You can now install Python packages and run Python scripts within the virtual environment, and they will be isolated from the system Python installation.

- To deactivate the virtual environment and return to the system Python, simply run the following command:
  ```bash
  deactivate
  ```
- Once your virtual environment is activated, use the following command to generate a list of installed packages and their versions:
  ```bash
  pip freeze
  ```  
- Remember to activate the virtual environment whenever you work on a project that requires it.
## 2. Install Dependencies
- Install the <code>python-binance</code> library, which is a Python wrapper for the Binance API. You can use the following pip command:
  
  ```bash
  pip install python-binance
  ```
![BinanceVolatilityBot](https://github.com/geobla/binanceVolatilityBot/assets/99928380/f8fb6175-755b-4955-a2ad-588e3a3d10ed)

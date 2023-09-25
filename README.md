# binanceVolatilityBot (Docker Ready)

## Overview
This Python-based cryptocurrency trading bot leverages the Binance API to automate the trading process. The bot's strategy is designed to identify and capitalize on short-term price movements in the cryptocurrency market. It aims to make informed buying decisions based on price volatility and predefined criteria.

## Key Features

### Pairing Currencies: 
The bot allows you to select the currency or fiat currency with which each cryptocurrency is paired. By default, it pairs cryptocurrencies with `'USDT'` (Tether), a commonly used stablecoin.

### Trade Size: 
You can define the size of each trade, typically in USDT, using the `QUANTITY` parameter. Be cautious when changing the pairing currency, as this affects the trade size calculation.

### Excluded Pairs: 
The bot provides the flexibility to exclude specific currency pairs from trading. By default, it excludes popular fiat pairs and some margin keywords.

### Price Difference: 
The bot monitors the price difference for each cryptocurrency over a specified time period (default is 5 minutes). It considers coins that have moved by a certain percentage (default is 3%) as potential buy signals.

### Stop Loss and Take Profit: 
The bot includes risk management features such as `Stop Loss` and `Take Profit` percentages. If a coin's price moves beyond these thresholds, the bot will automatically sell the coin to limit losses or secure profits.

### Portfolio Tracking: 
The bot maintains a portfolio of coins bought during trading. It tracks essential details such as the purchase price, volume, and order ID for each coin.

## Run Locally Without Docker

## 1. Create a Virtual Environment. 
   
To create a virtual environment in Python, you can use the <code>venv</code> module, which is included in Python 3.3 and later. Here's how to create a virtual environment:
- Open your command prompt or terminal.
- Navigate to the directory where you want to create the virtual environment.
  You can use the `cd` command to change directories.
  For example:
  ```bash
  cd /path/to/your/directory
  ```
- Inside the directory `git clone` the repository:
  ```bash
  git clone https://github.com/geobla/binanceVolatilityBot.git
  ```
- or download the [zip folder](https://github.com/geobla/binanceVolatilityBot/archive/refs/heads/main.zip) to your directory.
- Change the fake `API Keys` with your Private Spot or TestNet Binance Keys (<ins>Please start with TestNet to get familiar with the Bot</ins>) in the `.env` file.
- Once you are in the desired directory, run the following command to create a virtual environment.
  You can replace if you want <code>myenv</code> with the name you want to give your virtual environment:
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
- Once your virtual environment is activated, you could use the following command to generate a list of installed packages and their versions (just for FYI):
  ```bash
  pip freeze
  ```  
- Remember to activate the virtual environment whenever you work on a project that requires it.

## 2. Install Dependencies

- Install the <code>python-binance</code> library, which is a Python wrapper for the Binance API. You can use the following pip command:
  
  ```bash
  pip install python-binance
  ```
## 3. Run the Bot (<ins>Without Docker</ins>)

- To run your bot locally without Docker and considering the location of the `.env` file and the main script `VolatilityBot.py`, you'll need to adjust the paths in the code to correctly access the `.env` file. Since the `.env` file is located one step outside of the main script directory, you can use the `os` module to construct the full path to the .env file dynamically. Here are the changes you should make:
  
   - Modify the VolatilityBot.py script to access the .env file using a dynamic path based on the script's location:
     Inside the main code go to line 16 (under `import json`) and paste:
  ```python
  import os
  # Determine the full path to the .env file
  script_dir = os.path.dirname(os.path.abspath(__file__))
  env_file_path = os.path.join(script_dir, '..', '.env')
  ```
   - In the code above, we use `os.path.abspath(__file__)` to get the absolute path of the script, and then we construct the path to the .env file by going one step up from the script directory.

   - When running the bot, you should navigate to the `src` directory before executing the script. If you are currently in the binanceVolatilityBot directory, you can use the following command:
  ```bash
  cd src
  python3 VolatilityBot.py
  ```
  - With these changes, your script should be able to access the `.env` file correctly, even if it's located one step outside of the src directory where 
    `VolatilityBot.py` is located.
![BinanceVolatilityBot](https://github.com/geobla/binanceVolatilityBot/assets/99928380/f8fb6175-755b-4955-a2ad-588e3a3d10ed)

## 4. Run the Bot (<ins>With Docker</ins>)
- Go to your preferred directory.
- Inside the directory `git clone` the repository:
  ```bash
  git clone https://github.com/geobla/binanceVolatilityBot.git
  ```
- or download the [zip folder](https://github.com/geobla/binanceVolatilityBot/archive/refs/heads/main.zip) to your directory.
- Change the fake `API Keys` with your Private Spot or TestNet Binance Keys (<ins>Please start with TestNet to get familiar with the Bot</ins>) in the `.env` file.
- Make sure that you are inside the correct directory:
  ```bash
  pwd
  ```
  It should end with `binanceVolatilityBot`.
- Build and Run the Docker Image.
  To build and run your Docker image, use the commands.

  ```bash
  docker build -t my-binance-app .
  ```
  ```bash
  docker run -itd --env-file .env --name my-binance-app my-binance-app
  ``` 
  You can combine the `-it` and `-d` options in the docker run command to run your container in detached mode (-d) while also enabling an interactive terminal (-it). 
  This way, you can have the benefits of both detached mode and interactive mode for viewing logs.
- How to check the logs (Trades).
  ```bash
  docker logs my-binance-app
  ```
- Or better install [Portainer](https://docs.portainer.io/start/install-ce/server/docker/linux) (if not already) and go to the my-binance-app container log and see the 
  results.
  
  ![portainerBinanceBot](https://github.com/geobla/binanceVolatilityBot/assets/99928380/7cbd8b3a-8cec-4d40-bb89-9e32cf0571d1)

## Risk Considerations
Cryptocurrency trading involves inherent risks, including price volatility and market fluctuations. It's essential to exercise caution and conduct thorough testing before using this bot with real funds. Consider running the bot in a test environment (e.g., [Binance's Testnet](https://testnet.binance.vision/)) to evaluate its performance.





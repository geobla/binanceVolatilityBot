import os

# Needed for the binance API and websockets.
from binance.client import Client

# Needed for dates.
from datetime import datetime, timedelta
import time

# Needed for repeatedly executing the code.
from itertools import count

# Used to store trades and sell assets
import json

# Open and read the .env file
with open('.env', 'r') as env_file:
    env_lines = env_file.readlines()

# Create a dictionary to store the environment variables
env_vars = {}
for line in env_lines:
    line = line.strip()
    if line and not line.startswith('#'):  # Ignore empty lines and comments
        key, value = line.split('=', 1)
        env_vars[key] = value

# Access your API keys using the config object
api_key = env_vars.get("API_KEY")
secret_key = env_vars.get("API_SECRET")

# Define if you are using Testnet or Spot
TESTNET = True

# Authenticate with the client
if TESTNET:
    client = Client(api_key, secret_key)

    # The API URL needs to be manually changed in the library to work on the TESTNET
    client.API_URL = 'https://testnet.binance.vision/api'
else:
    client = Client(api_key, secret_key)

# select what to pair the coins to and pull all coins paied with PAIR_WITH
# PAIR_WITH defines the currency (or fiat currency) with which each cryptocurrency is paired.
# I have only tested this with USDT since most cryptocurrencies are paired with it.
PAIR_WITH = 'USDT'

# Define the size of each trade, by default in USDT
# QUANTITY represents the size of your trade, by default in USDT.
# Be very careful with the QUANTITY if you change PAIR_WITH to BNB, for example."
QUANTITY = 100

# List of pairs to exlcude
# by default we're excluding the most popular fiat pairs
# and some margin keywords, if we're only working on the SPOT account
FIATS = ['EURUSDT', 'GBPUSDT', 'JPYUSDT', 'USDUSDT', 'DOWN', 'UP']

# the amount of time in MINUTES to calculate the differnce from the current price

# TIME_DIFFERENCE by default, we are checking the price difference of each
# cryptocurrency on Binance in the last 5 minutes.
# You can change this value to obtain different results.
# This also determines the frequency at which each code iteration is executed
TIME_DIFFERENCE = 5

# the difference in % between the first and second checks for the price,
# by default set at 10 minutes apart.
CHANGE_IN_PRICE = 3
# CHANGE_IN_PRICE is the threshold at which the bot will decide to buy a cryptocurrency.
# By default, if a cryptocurrency has moved more than 3% in the last 5 minutes,
# we consider it a strong buy signal.

# define in % when to sell a coin that's not making a profit
STOP_LOSS = 3
# define in % when to take profit on a profitable coin
TAKE_PROFIT = 6

# coins that were bought by the bot since its start
coins_bought = {}

# path to the saved coins_bought file
coins_bought_file_path = 'coins_bought.json'

# use separate files for testnet and live
if TESTNET:
    coins_bought_file_path = 'testnet_' + coins_bought_file_path

# if saved coins_bought json file exists then load it
if os.path.isfile(coins_bought_file_path):
    with open(coins_bought_file_path) as file:
        coins_bought = json.load(file)

# The get_price() function will the return the price of each coin that meets our criteria.


def get_price():
    '''Return the current price for all coins on binance'''

    initial_price = {}
    prices = client.get_all_tickers()

    for coin in prices:

        # only Return USDT pairs and exlcude margin symbols like BTCDOWNUSDT
        if PAIR_WITH in coin['symbol'] and all(item not in coin['symbol'] for item in FIATS):
            initial_price[coin['symbol']] = {
                'price': coin['price'], 'time': datetime.now()}

    return initial_price

# TIME_DIFFERENCE variable and will return any coin that has moved by more than
# the CHANGE_IN_PRICE – by default 3%.


def wait_for_price():
    '''calls the initial price and ensures the correct amount of time has passed
    before reading the current price again'''

    volatile_coins = {}
    initial_price = get_price()

    while initial_price['BNBUSDT']['time'] > datetime.now() - timedelta(minutes=TIME_DIFFERENCE):
        print(f'not enough time has passed yet...')

        # let's wait here until the time passess...
        time.sleep(60*TIME_DIFFERENCE)

    else:
        last_price = get_price()

        # calculate the difference between the first and last price reads
        for coin in initial_price:
            threshold_check = (float(initial_price[coin]['price']) - float(
                last_price[coin]['price'])) / float(last_price[coin]['price']) * 100

            # each coin with higher gains than our CHANGE_IN_PRICE is added to
            # the volatile_coins dict

            if threshold_check > CHANGE_IN_PRICE:
                volatile_coins[coin] = threshold_check
                volatile_coins[coin] = round(volatile_coins[coin], 3)

                print(
                    f'{coin} has gained {volatile_coins[coin]}% in the last {TIME_DIFFERENCE} minutes, calculating volume in {PAIR_WITH}')

        if len(volatile_coins) < 1:
            print(
                f'No coins moved more than {CHANGE_IN_PRICE}% in the last {TIME_DIFFERENCE} minute(s)')

        return volatile_coins, len(volatile_coins), last_price

# The next step is to convert our QUANTITY of 100USDT (default)
# into the respective quantity for each coin that we’re about to buy.


def convert_volume():
    '''Converts the volume given in QUANTITY from USDT to the each coin's volume'''
# Because Binance is a bit particular with the format of the volume, our trading bot needs
# to know the step size for each coin.

    volatile_coins, number_of_coins, last_price = wait_for_price()
    lot_size = {}
    volume = {}

    for coin in volatile_coins:

        # Find the correct step size for each coin
        # max accuracy for BTC for example is 6 decimal points
        # while XRP is only 1
        try:
            info = client.get_symbol_info(coin)
            step_size = info['filters'][2]['stepSize']
            lot_size[coin] = step_size.index('1') - 1

            if lot_size[coin] < 0:
                lot_size[coin] = 0

        except:
            pass

        # calculate the volume in coin from QUANTITY in USDT (default)
        volume[coin] = float(QUANTITY / float(last_price[coin]['price']))

        # define the volume with the correct step size
        if coin not in lot_size:
            volume[coin] = float('{:.1f}'.format(volume[coin]))
        else:
            volume[coin] = float('{:.{}f}'.format(
                volume[coin], lot_size[coin]))
    return volume, last_price


def trade():
    '''Place Buy market orders for each volatile coin found'''

    volume, last_price = convert_volume()
    orders = {}

    for coin in volume:

        # only buy if the there are no active trades on the coin
        if coin not in coins_bought or coins_bought[coin] == None:
            print(f' preparing to buy {volume[coin]} {coin}')

            if TESTNET:
                # create test order before pushing an actual order
                test_order = client.create_test_order(
                    symbol=coin, side='BUY', type='MARKET', quantity=volume[coin])

            # try to create a real order if the test orders did not raise an exception
            try:
                buy_limit = client.create_order(
                    symbol=coin,
                    side='BUY',
                    type='MARKET',
                    quantity=volume[coin]
                )

            # error handling here in case position cannot be placed
            except Exception as e:
                print(e)

            # run the else block if the position has been placed and return order info
            else:
                orders[coin] = client.get_all_orders(symbol=coin, limit=1)
        else:
            print(
                f'Signal detected, but there is already an active trade on {coin}')

    return orders, last_price, volume

# The next step is to update our portfolio by saving the details of each trade
# into the json file that we’re checking for at the beginning of each iteration.


def update_porfolio(orders, last_price, volume):
    '''add every coin bought to our portfolio for tracking/selling later'''

    for coin in orders:
        coins_bought[coin] = {
            'symbol': orders[coin][0]['symbol'],
            'orderid': orders[coin][0]['orderId'],
            'timestamp': orders[coin][0]['time'],
            'bought_at': last_price[coin]['price'],
            'volume': volume[coin]
        }

        # save the coins in a json file in the same directory
        with open(coins_bought_file_path, 'w') as file:
            json.dump(coins_bought, file, indent=4)

# checks if any of the coins we own in our bot portfolio should be sold due to SL or TP being reached.


def sell_coins():
    '''sell coins that have reached the STOP LOSS or TAKE PROFIT thershold'''

    last_price = get_price()

    for coin in coins_bought:
        # define stop loss and take profit
        TP = float(coins_bought[coin]['bought_at']) + \
            (float(coins_bought[coin]['bought_at']) * TAKE_PROFIT) / 100
        SL = float(coins_bought[coin]['bought_at']) - \
            (float(coins_bought[coin]['bought_at']) * STOP_LOSS) / 100

        # check that the price is above the take profit or below the stop loss
        if float(last_price[coin]['price']) > TP or float(last_price[coin]['price']) < SL:
            print(
                f"TP or SL reached, selling {coins_bought[coin]['volume']} {coin}...")

            if TESTNET:
                # create test order before pushing an actual order
                test_order = client.create_test_order(
                    symbol=coin, side='SELL', type='MARKET', quantity=coins_bought[coin]['volume'])

            # try to create a real order if the test orders did not raise an exception
            try:
                sell_coins_limit = client.create_order(
                    symbol=coin,
                    side='SELL',
                    type='MARKET',
                    quantity=coins_bought[coin]['volume']
                )

            # error handling here in case position cannot be placed
            except Exception as e:
                print(e)

            # run the else block if the position has been placed and update
            # the coins bought json file
            else:
                coins_bought[coin] = None
                with open(coins_bought_file_path, 'w') as file:
                    json.dump(coins_bought, file, indent=4)
        else:
            print(f'TP or SL not yet reached, not selling {coin} for now...')


print('Press Ctrl-Q to stop the script')
for i in count():
    orders, last_price, volume = trade()
    update_porfolio(orders, last_price, volume)
    sell_coins()

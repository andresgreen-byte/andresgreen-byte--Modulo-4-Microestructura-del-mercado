import ccxt
import numpy as np
import pandas as pd
import time
from datetime import datetime

def get_btc_bitso(limit,symbol):
    bitso=ccxt.bitso()
    crypto = bitso.fetch_order_book(symbol,limit=limit)
    dt = datetime.now()
    bi_btc_ob_ask = pd.DataFrame(crypto['asks'],columns=['price','quantity'])
    bi_btc_ob_bid = pd.DataFrame(crypto['bids'],columns=['price','quantity'])
    bid = crypto['bids'][0][0] if len(crypto['bids']) > 0 else None
    ask = crypto['asks'][0][0] if len(crypto['asks']) > 0 else None
    spread = (ask - bid) if (ask and bid) else None
    mid = (ask+bid)/2
    d = {'timestamp':[dt],'Bid': [bid],'Ask':[ask],'Mid':[mid],'Spread':[spread]}
    return d



def get_ochlv_btc_bitso(from_datime):
    bitso=ccxt.bitso()
    since = bitso.parse8601(from_datime)
    ohlcv = pd.DataFrame(bitso.fetch_ohlcv('BTC/USDT', timeframe='1m', since=since, limit=100))
    return ohlcv

def get_btc_binance(limit,symbol):
    bitso=ccxt.binance()
    crypto = bitso.fetch_order_book(symbol,limit=limit)
    dt = datetime.now()
    bi_btc_ob_ask = pd.DataFrame(crypto['asks'],columns=['price','quantity'])
    bi_btc_ob_bid = pd.DataFrame(crypto['bids'],columns=['price','quantity'])
    bid = crypto['bids'][0][0] if len(crypto['bids']) > 0 else None
    ask = crypto['bids'][0][0] if len(crypto['asks']) > 0 else None
    spread = (ask - bid) if (ask and bid) else None
    mid = (ask+bid)/2
    d = {'timestamp':[dt],'Bid': [bid],'Ask':[ask],'Mid':[mid],'Spread':[spread]}
    return d

def get_ochlv_binance(from_datime):
    bitso=ccxt.binance('ETH/USDT')
    since = bitso.parse8601(from_datime)
    ohlcv = pd.DataFrame(bitso.fetch_ohlcv('BTC/USDT', timeframe='1m', since=since, limit=100))
    return ohlcv



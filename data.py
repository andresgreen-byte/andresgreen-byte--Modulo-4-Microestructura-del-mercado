import ccxt
import numpy as np
import pandas as pd

bitso = ccxt.bitso()

limit = 30

bi_btc_ob = bitso.fetch_order_book('BTC/USDT',limit=limit)

bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'],columns=['price','quantity'])
bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'],columns=['price','quantity'])

bid = bi_btc_ob['bids'][0][0] if len(bi_btc_ob['bids']) > 0 else None
ask = bi_btc_ob['bids'][0][0] if len(bi_btc_ob['asks']) > 0 else None
spread = (ask - bid) if (ask and bid) else None

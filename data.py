import ccxt
import numpy as np
import pandas as pd
import time
from datetime import datetime
import functions as f

btc_bitso = []
for i in range(10):
    x = f.get_btc_bitso(30,'BTC/USDT')
    time.sleep(1)
    btc_bitso.append(x)
btc_bitso = pd.DataFrame(btc_bitso)

ts1 = btc_bitso['timestamp'].iloc[0]

ochlv_btc =f.get_ochlv_btc_bitso(ts1)
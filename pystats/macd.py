import pandas as pd

def calculate_macd(data, short_period=12, long_period=26, signal_period=9):
    """Calculate the MACD and signal line."""
    data['ema_short'] = data['close'].ewm(span=short_period, adjust=False).mean()
    data['ema_long'] = data['close'].ewm(span=long_period, adjust=False).mean()

    data['MACD'] = data['ema_short'] - data['ema_long']
    data['signal_line'] = data['MACD'].ewm(span=signal_period, adjust=False).mean()

    data['MACD_histogram'] = data['MACD'] - data['signal_line']

    return data[['time', 'MACD', 'signal_line', 'MACD_histogram']]

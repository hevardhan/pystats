import pandas as pd
import numpy as np

def calculate_sma(data, window):
    """Calculate the Simple Moving Average (SMA) for a given window."""
    return data['close'].rolling(window=window).mean()

def sma_crossover_strategy(data, short_window=50, long_window=200):
    """Implement a simple SMA crossover strategy."""
    data['SMA_short'] = calculate_sma(data, short_window)
    data['SMA_long'] = calculate_sma(data, long_window)

    data['signal'] = 0
    data['signal'][short_window:] = np.where(data['SMA_short'][short_window:] > data['SMA_long'][short_window:], 1, 0)
    data['positions'] = data['signal'].diff()

    return data[['time', 'close', 'SMA_short', 'SMA_long', 'signal', 'positions']]

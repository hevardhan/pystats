import pandas as pd

def heiken_ashi(data):
    """Calculate Heiken Ashi candles."""
    ha_data = pd.DataFrame(index=data.index)
    ha_data['HA_close'] = (data['open'] + data['high'] + data['low'] + data['close']) / 4
    ha_data['HA_open'] = (data['open'].shift(1) + data['close'].shift(1)) / 2
    ha_data['HA_high'] = data[['high', 'HA_open', 'HA_close']].max(axis=1)
    ha_data['HA_low'] = data[['low', 'HA_open', 'HA_close']].min(axis=1)

    # Handle first row initialization
    ha_data['HA_open'].iloc[0] = data['open'].iloc[0]

    return ha_data[['HA_open', 'HA_high', 'HA_low', 'HA_close']]

import talib

def calculate_close_indicators(stock_data):
    """
    Calculate technical indicators for the 'Close' column.
    Args:
        df (pd.DataFrame): Stock data with a 'Close' column.
    Returns:
        pd.DataFrame: DataFrame with indicators for 'Close'.
    """
    stock_data['SMA_Close_50'] = talib.SMA(stock_data['Close'], timeperiod=50)
    stock_data['EMA_Close_50'] = talib.EMA(stock_data['Close'], timeperiod=50)
    stock_data['RSI_Close'] = talib.RSI(stock_data['Close'], timeperiod=14)
    macd, macd_signal, macd_hist = talib.MACD(stock_data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    stock_data['MACD_Close'] = macd
    stock_data['MACD_Signal_Close'] = macd_signal
    stock_data['MACD_Hist_Close'] = macd_hist
    return stock_data


def calculate_high_indicators(df):
    """
    Calculate technical indicators for the 'High' column.
    Args:
        df (pd.DataFrame): Stock data with a 'High' column.
    Returns:
        pd.DataFrame: DataFrame with indicators for 'High'.
    """
    df['SMA_High_50'] = talib.SMA(df['High'], timeperiod=50)
    df['EMA_High_50'] = talib.EMA(df['High'], timeperiod=50)
    df['RSI_High'] = talib.RSI(df['High'], timeperiod=14)
    return df


def calculate_low_indicators(df):
    """
    Calculate technical indicators for the 'Low' column.
    Args:
        df (pd.DataFrame): Stock data with a 'Low' column.
    Returns:
        pd.DataFrame: DataFrame with indicators for 'Low'.
    """
    df['SMA_Low_50'] = talib.SMA(df['Low'], timeperiod=50)
    df['EMA_Low_50'] = talib.EMA(df['Low'], timeperiod=50)
    df['RSI_Low'] = talib.RSI(df['Low'], timeperiod=14)
    return df


def calculate_open_indicators(df):
    """
    Calculate technical indicators for the 'Open' column.
    Args:
        df (pd.DataFrame): Stock data with an 'Open' column.
    Returns:
        pd.DataFrame: DataFrame with indicators for 'Open'.
    """
    df['SMA_Open_50'] = talib.SMA(df['Open'], timeperiod=50)
    df['EMA_Open_50'] = talib.EMA(df['Open'], timeperiod=50)
    df['RSI_Open'] = talib.RSI(df['Open'], timeperiod=14)
    return df


def calculate_volume_indicators(df):
    """
    Calculate indicators for the 'Volume' column.
    Args:
        df (pd.DataFrame): Stock data with a 'Volume' column.
    Returns:
        pd.DataFrame: DataFrame with indicators for 'Volume'.
    """
    df['SMA_Volume_50'] = talib.SMA(df['Volume'], timeperiod=50)
    return df


def calculate_all_indicators(df):
    """
    Wrapper function to calculate all indicators for all essential columns.
    Args:
        df (pd.DataFrame): Stock data with columns Open, High, Low, Close, Volume.
    Returns:
        pd.DataFrame: DataFrame with all indicators calculated.
    """
    df = calculate_close_indicators(df)
    df = calculate_high_indicators(df)
    df = calculate_low_indicators(df)
    df = calculate_open_indicators(df)
    df = calculate_volume_indicators(df)
    return df

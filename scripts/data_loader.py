import pandas as pd

def load_stock_data(file_path):
    """
    Load stock data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the stock data with parsed dates.
    """
    return pd.read_csv(file_path, parse_dates=["date"])
    

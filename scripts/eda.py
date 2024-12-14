import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)


# Data Loading Function (if not already present)
def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path, parse_dates=["Date"])

# Data Cleaning Functions
def check_missing_values(df):
    """
    Check for missing values in the dataset.
    Returns a summary of missing values per column.
    """
    missing_values = df.isnull().sum()
    return missing_values[missing_values > 0]

def handle_missing_values(df, strategy="drop", fill_value=None):
    """
    Handle missing values in the dataset.
    
    Parameters:
        df (DataFrame): Input dataframe.
        strategy (str): 'drop' to drop rows, 'fill' to fill missing values.
        fill_value: Value to fill in case of 'fill' strategy.
        
    Returns:
        DataFrame: Cleaned dataset.
    """
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill":
        return df.fillna(fill_value)
    else:
        raise ValueError("Invalid strategy. Choose 'drop' or 'fill'.")

def detect_outliers(df, column, method="iqr"):
    """
    Detect outliers in a numerical column.
    
    Parameters:
        df (DataFrame): Input dataframe.
        column (str): Column name to check for outliers.
        method (str): 'iqr' for Interquartile Range, 'zscore' for Z-score method.
        
    Returns:
        DataFrame: Rows with outliers in the specified column.
    """
    if method == "iqr":
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    elif method == "zscore":
        mean = df[column].mean()
        std = df[column].std()
        z_scores = (df[column] - mean) / std
        return df[(z_scores > 3) | (z_scores < -3)]
    else:
        raise ValueError("Invalid method. Choose 'iqr' or 'zscore'.")

                

def remove_outliers(df, column, method="iqr"):
    """
    Remove outliers from a numerical column.
    
    Parameters:
        df (DataFrame): Input dataframe.
        column (str): Column name to clean of outliers.
        method (str): 'iqr' for Interquartile Range, 'zscore' for Z-score method.
        
    Returns:
        DataFrame: Cleaned dataset.
    """
    outliers = detect_outliers(df, column, method)
    return df.drop(outliers.index)

def get_headline_length_stats(df, column='headline'):
    """Calculates basic statistics for headline lengths."""
    df['headline_length'] = df[column].str.len()
    return df['headline_length'].describe()

def count_articles_per_publisher(df, column='publisher'):
    """Counts the number of articles per publisher."""
    return df[column].value_counts()

def analyze_publication_trends(df, column='date'):
    """Analyzes publication trends over time."""
    df[column] = pd.to_datetime(df[column])
    return df[column].dt.date.value_counts().sort_index()

def plot_trends(series, title):
    """Plots trends in data."""
    series.plot(kind='line')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.show()

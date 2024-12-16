import matplotlib.pyplot as plt

def plot_column_with_indicators(df, column, indicators):
    """
    Plot a specific column with its technical indicators.
    Args:
        df (pd.DataFrame): Stock data with indicators.
        column (str): The column to plot (e.g., 'Close', 'High').
        indicators (list of str): Indicator columns to plot alongside the main column.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df[column], label=f'{column}')
    for indicator in indicators:
        plt.plot(df[indicator], label=indicator, linestyle='--')
    plt.title(f'{column} with Indicators')
    plt.legend()
    plt.show()


def plot_rsi(df, column):
    """
    Plot RSI for a specific column.
    Args:
        df (pd.DataFrame): Stock data with RSI indicators.
        column (str): The column for which RSI is plotted (e.g., 'Close', 'High').
    """
    rsi_column = f'RSI_{column}'
    plt.figure(figsize=(12, 6))
    plt.plot(df[rsi_column], label=f'RSI ({column})')
    plt.axhline(70, color='red', linestyle='--', label='Overbought')
    plt.axhline(30, color='green', linestyle='--', label='Oversold')
    plt.title(f'RSI for {column}')
    plt.legend()
    plt.show()

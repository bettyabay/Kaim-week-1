import pandas as pd
import numpy as np

def analyze_publication_frequency(df, column='date'):
    """Analyzes publication frequency over time."""
    df[column] = pd.to_datetime(df[column])
    frequency = df[column].dt.date.value_counts().sort_index()
    return frequency

def identify_publication_spikes(frequency, threshold):
    """Identifies spikes in publication frequency."""
    spikes = frequency[frequency > threshold]
    return spikes

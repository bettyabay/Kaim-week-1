import pandas as pd
import numpy as np
import re

# Publisher Analysis Functions

def count_articles_per_publisher(df):
    """
    Count the number of articles per publisher.
    Returns a Series of counts.
    """
    return df['publisher'].value_counts()

def extract_publisher_domain(df):
    """
    Extract the domain from email-based publisher names.
    If 'publisher' is an email, return the domain part.
    """
    df['publisher_domain'] = df['publisher'].apply(lambda x: extract_domain(x))
    return df

def extract_domain(email):
    """
    Extract domain from an email string.
    """
    match = re.search(r'@([A-Za-z0-9.-]+)', email)
    if match:
        return match.group(1)
    else:
        return None

def analyze_publisher_types(df):
    """
    Analyze and classify the types of news reported by each publisher.
    This can include analyzing common keywords in headlines or topics.
    """
    publisher_types = {}
    
    # Group by publisher
    grouped = df.groupby('publisher')['headline'].apply(lambda x: ' '.join(x)).reset_index()

    # Keyword extraction or topic modeling (dummy example, refine as needed)
    for idx, row in grouped.iterrows():
        # This could be more sophisticated, e.g., topic modeling or keyword analysis
        keywords = row['headline'].split()
        publisher_types[row['publisher']] = keywords
    
    return publisher_types


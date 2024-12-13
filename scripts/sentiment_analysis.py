from textblob import TextBlob

def calculate_sentiment(headline):
    """Calculates sentiment polarity for a given headline."""
    analysis = TextBlob(headline)
    return analysis.sentiment.polarity  # Polarity ranges from -1 to 1

def classify_sentiment(polarity):
    """Classifies sentiment as positive, negative, or neutral."""
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def add_sentiment_column(df, column='headline'):
    """Adds sentiment polarity and classification to the dataframe."""
    df['polarity'] = df[column].apply(calculate_sentiment)
    df['sentiment'] = df['polarity'].apply(classify_sentiment)
    return df


from sklearn.feature_extraction.text import CountVectorizer

def extract_common_keywords(df, column='headline', n_keywords=10):
    """Extracts common keywords from headlines."""
    vectorizer = CountVectorizer(stop_words='english', max_features=n_keywords)
    word_counts = vectorizer.fit_transform(df[column])
    keywords = vectorizer.get_feature_names_out()
    return keywords


def display_topics(model, feature_names, no_top_words):
    """
    Display the top words for each topic.

    Parameters:
        model: Trained topic model (e.g., LDA).
        feature_names: List of feature names from vectorization.
        no_top_words: Number of top words to display for each topic.
    """
    for topic_idx, topic in enumerate(model.components_):
        print(f"Topic {topic_idx}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))


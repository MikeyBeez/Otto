import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(prompt):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(prompt)
    if sentiment['compound'] >= 0.05:
        return "Positive"
    elif sentiment['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example usage:
prompt = "I love this product!"
sentiment = sentiment_analysis(prompt)
print(sentiment)  # Output: Positive

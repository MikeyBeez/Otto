# test_otto_sentiment.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from modules.otto_sentiment import sentiment_analysis

class TestOttoSentiment(unittest.TestCase):
    def test_positive_sentiment(self):
        prompt = "I love this product!"
        sentiment = sentiment_analysis(prompt)
        self.assertEqual(sentiment, "Positive")

    def test_negative_sentiment(self):
        prompt = "I hate this product!"
        sentiment = sentiment_analysis(prompt)
        self.assertEqual(sentiment, "Negative")

    def test_neutral_sentiment(self):
        prompt = "This product is made of plastic."
        sentiment = sentiment_analysis(prompt)
        self.assertEqual(sentiment, "Neutral")

if __name__ == "__main__":
    unittest.main()

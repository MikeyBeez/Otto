Module: otto_sentiment
Description: This module provides a function for analyzing the sentiment of a given text prompt. It uses the NLTK library's VADER (Valence Aware Dictionary and sEntiment Reasoner) tool to determine the sentiment of the text.
Functions:
sentiment_analysis(prompt): Analyzes the sentiment of the given text prompt and returns a string indicating whether the sentiment is positive, negative, or neutral.
Parameters:
prompt: The text prompt to be analyzed.
Returns:
A string indicating the sentiment of the text prompt. Possible values are "Positive", "Negative", or "Neutral".
Example Usage:
Python
prompt = "I love this product!"
sentiment = sentiment_analysis(prompt)
print(sentiment)  # Output: Positive
Notes:
The sentiment analysis is based on the compound score calculated by VADER. If the score is greater than or equal to 0.05, the sentiment is considered positive. If the score is less than or equal to -0.05, the sentiment is considered negative. Otherwise, the sentiment is considered neutral.
This module requires the NLTK library to be installed and configured.

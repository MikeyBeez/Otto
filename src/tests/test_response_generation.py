# src/tests/test_response_generator.py

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modules')))

from response_generator import ResponseGenerator

def test_generate_response():
    model_name = "llama3-chatqa"
    lda_model_file = "lda_model.pkl"
    response_generator = ResponseGenerator(model_name, lda_model_file)

    # Test case 1: Simple input
    user_input = "I love this product!"
    response = response_generator.generate_response(user_input)
    assert isinstance(response['response'], str)
    assert len(response['response']) > 0
    assert response['sentiment'] == "Positive"
    assert 'product' in response['entities']
    assert len(response['topic_distribution']) > 0

    # Test case 2: Complex input
    user_input = "The book 'The Great Gatsby' is a classic novel written by F. Scott Fitzgerald."
    response = response_generator.generate_response(user_input)
    assert isinstance(response['response'], str)
    assert len(response['response']) > 0
    assert response['sentiment'] == "Neutral"
    assert 'The Great Gatsby' in response['entities']
    assert 'F. Scott Fitzgerald' in response['entities']
    assert len(response['topic_distribution']) > 0

    print("All tests passed!")

if __name__ == "__main__":
    test_generate_response()

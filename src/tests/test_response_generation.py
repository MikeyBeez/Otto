# src/tests/test_response_generator.py

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modules')))

from response_generator import ResponseGenerator

def test_generate_response():
    model_name = "llama3-chatqa"
    response_generator = ResponseGenerator(model_name)

    # Test case 1: Simple input
    user_input = "Hello, how are you?"
    response = response_generator.generate_response(user_input)
    assert isinstance(response, str)
    assert len(response) > 0

    # Test case 2: Complex input
    user_input = "Why is the sky blue?"
    response = response_generator.generate_response(user_input)
    assert isinstance(response, str)
    assert len(response) > 0

    print("All tests passed!")

if __name__ == "__main__":
    test_generate_response()

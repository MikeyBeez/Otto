# src/modules/response_generator.py

import ollama

class ResponseGenerator:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_response(self, user_input):
        response = ollama.chat(
            model=self.model_name,
            messages=[{'role': 'user', 'content': user_input}],
            stream=True
        )
        captured_output = ""
        for chunk in response:
            captured_output += chunk['message']['content']
        return captured_output

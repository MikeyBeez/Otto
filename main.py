import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'src' directory to the Python path using a relative path
sys.path.append(os.path.join(current_dir, '..', 'src'))

from response_generator import ResponseGenerator
from document_storage import DocumentStorage

# Initialize modules
response_generator = ResponseGenerator()
document_storage = DocumentStorage()

# Main loop
while True:
    user_input = input("User: ")
    
    # Generate response
    response = response_generator.generate_response(user_input)
    
    # Print assistant response
    print(f"Assistant: {response}")
    
    # Save user input and assistant response to document storage
    document_storage.save_interaction(user_input, response)
    
    # Check if user wants to exit
    if user_input.lower() in ["quit", "exit", "bye"]:
        break

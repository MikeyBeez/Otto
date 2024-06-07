# modules/otto_intent_detection.py
import langchain
from langchain_community.llms import Ollama

llm = Ollama(model="llama3-chatqa")

def get_intent(text):
    possible_intents = [
        "Book_Flight", "Chat", "Search_Airport", "Search_Hotel", "Book_Hotel",
        "Cancel_Booking", "Check_In", "Flight_Status", "Travel_Advice",
        "Make_Reservation", "Weather_Query", "Tell_Joke", "Unknown"
    ]
    intent_string = ", ".join(possible_intents)

    examples = [
        ("Book a flight to New York", "Book_Flight"),
        ("Find a hotel in Paris", "Book_Hotel"),
        ("What is the weather like in London?", "Weather_Query"),
        ("Tell me a joke", "Tell_Joke"),
        ("Make a reservation at an Italian restaurant", "Make_Reservation")
    ]

    prompt = "Determine the intent of the following text based on the provided examples:\n\n"
    
    for example, intent in examples:
        prompt += f"Text: {example}\nIntent: {intent}\n\n"
    
    prompt += f"Text: {text}\nIntent:"

    response = llm.invoke(prompt)
    intent = response.strip()
    if intent not in possible_intents:
        intent = "Unknown"
    return intent

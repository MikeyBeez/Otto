Here is the documentation for the otto_intent_detection module:
Module: otto_intent_detection
Description: This module uses the LangChain library and the LLaMA3-ChatQA model to detect the intent behind a given text. It uses a prompt-based approach, providing examples of text and their corresponding intents to the model, and then asking it to determine the intent of the input text.
Functions:
get_intent(text): Takes a text input and returns the detected intent as a string.
Possible Intents:
Book_Flight
Chat
Search_Airport
Search_Hotel
Book_Hotel
Cancel_Booking
Check_In
Flight_Status
Travel_Advice
Make_Reservation
Weather_Query
Tell_Joke
Unknown (default if no other intent is detected)
Examples:
get_intent("Book a flight to New York") -> Book_Flight
get_intent("Find a hotel in Paris") -> Book_Hotel
get_intent("What is the weather like in London?") -> Weather_Query
get_intent("Tell me a joke") -> Tell_Joke
get_intent("Make a reservation at an Italian restaurant") -> Make_Reservation
Note: The model may not always detect the intent correctly, and the output may vary based on the input text and the model's understanding of the prompt.

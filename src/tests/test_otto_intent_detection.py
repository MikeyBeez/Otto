# test_otto_intent_detection.py
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.otto_intent_detection import get_intent

class TestOttoIntentDetection(unittest.TestCase):
    def test_book_flight_intent(self):
        text = 'Book a flight to New York'
        intent = get_intent(text)
        self.assertEqual(intent, 'Book_Flight')

    def test_book_hotel_intent(self):
        text = 'Find a hotel in Paris'
        intent = get_intent(text)
        self.assertEqual(intent, 'Book_Hotel')

    def test_make_reservation_intent(self):
        text = 'Make a reservation at an Italian restaurant'
        intent = get_intent(text)
        self.assertEqual(intent, 'Make_Reservation')

    def test_weather_query_intent(self):
        text = 'What is the weather like in London?'
        intent = get_intent(text)
        self.assertEqual(intent, 'Weather_Query')

    def test_tell_joke_intent(self):
        text = 'Tell me a joke'
        intent = get_intent(text)
        self.assertEqual(intent, 'Tell_Joke')


if __name__ == '__main__':
    unittest.main()

# src/tests/test_otto_entity_rec.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from modules.otto_entity_rec import recognize_entities

class TestOttoEntityRecognition(unittest.TestCase):
    def test_single_entity(self):
        text = "John Smith is a great guy."
        entities = recognize_entities(text)
        self.assertEqual(entities, ["John Smith"])

    def test_multiple_entities(self):
        text = "John Smith and Jane Doe are friends."
        entities = recognize_entities(text)
        self.assertEqual(entities, ["John Smith", "Jane Doe"])

    def test_no_entities(self):
        text = "This is a test sentence."
        entities = recognize_entities(text)
        self.assertEqual(entities, [])

if __name__ == "__main__":
    unittest.main()

# src/tests/test_named_entity_recognition.py

import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from modules.named_entity_recognition import load_nlp_model, recognize_entities, explain_entity

class TestNamedEntityRecognition(unittest.TestCase):
    def setUp(self):
        self.nlp = load_nlp_model()

    def test_recognize_entities(self):
        text = "The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
        expected_entities = [
            ("The Indian Space Research Organisation", "ORG"),
            ("India", "GPE"),
            ("Bengaluru", "GPE"),
            ("Department of Space", "ORG"),
            ("India", "GPE"),
            ("ISRO", "ORG"),
            ("DOS", "ORG"),
        ]
        self.assertEqual(recognize_entities(text, self.nlp), expected_entities)

    def test_explain_entity(self):
        self.assertEqual(explain_entity("ORG"), "Companies, agencies, institutions, etc.")
        self.assertEqual(explain_entity("GPE"), "Countries, cities, states")

if __name__ == "__main__":
    unittest.main()

# src/tests/test_topic_modeling.py
import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.topic_modeling import preprocess_text, load_data, create_lda_model, get_topic_words

class TestTopicModeling(unittest.TestCase):
    def setUp(self):
        self.text_data = [
            "This is the first document.",
            "This document is the second document.",
            "And this is the third one.",
            "Is this the first document?",
        ]
        self.preprocessed_data = [preprocess_text(text) for text in self.text_data]
        self.num_topics = 2
        self.num_words = 3

    def test_preprocess_text(self):
        preprocessed_text = preprocess_text(self.text_data[0])
        self.assertEqual(preprocessed_text, ['this', 'is', 'the', 'first', 'document'])

    def test_create_lda_model(self):
        lda_model = create_lda_model(self.preprocessed_data, self.num_topics)
        self.assertEqual(lda_model.num_topics, self.num_topics)

    def test_get_topic_words(self):
        lda_model = create_lda_model(self.preprocessed_data, self.num_topics)
        topic_words = get_topic_words(lda_model, self.num_words)
        self.assertEqual(len(topic_words), self.num_topics)
        self.assertEqual(len(topic_words[0]), self.num_words)

if __name__ == "__main__":
    unittest.main()

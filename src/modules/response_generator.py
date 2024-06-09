# src/modules/response_generator.py

import ollama
from otto_sentiment import sentiment_analysis
from otto_entity_rec import recognize_entities
from topic_modeling import load_lda_model, get_topic_distribution, preprocess_text

class ResponseGenerator:
    def __init__(self, model_name, lda_model_file):
        self.model_name = model_name
        self.lda_model_file = lda_model_file
        self.lda_model = None
        self.dictionary = None

    def load_lda_model(self):
        self.lda_model = load_lda_model(self.lda_model_file)
        self.dictionary = self.lda_model.id2word

    def generate_response(self, user_input):
        if self.lda_model is None:
            self.load_lda_model()

        # Perform sentiment analysis
        sentiment = sentiment_analysis(user_input)

        # Perform entity recognition
        entities = recognize_entities(user_input)

        # Get topic distribution
        topic_distribution = get_topic_distribution(self.lda_model, self.dictionary, user_input)

        # Generate response using Ollama
        response = ollama.chat(
            model=self.model_name,
            messages=[{'role': 'user', 'content': user_input}],
            stream=True
        )
        captured_output = ""
        for chunk in response:
            captured_output += chunk['message']['content']

        # Return the generated response along with sentiment, entities, and topic distribution
        return {
            'response': captured_output,
            'sentiment': sentiment,
            'entities': entities,
            'topic_distribution': topic_distribution
        }

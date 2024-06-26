# src/modules/topic_modeling.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import PERSIST
import gensim
from gensim.utils import simple_preprocess
from gensim.matutils import corpus2dense
import pickle

# Set the directory path for saving and loading models
MODELS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
os.makedirs(MODELS_DIR, exist_ok=True)

def preprocess_text(text):
    # Tokenize and preprocess text
    tokens = simple_preprocess(text)
    return tokens

def load_data(data_dir):
    files = os.listdir(data_dir)
    text_data = []
    for file in files:
        with open(os.path.join(data_dir, file), 'r') as f:
            text = f.read()
            text_data.append(preprocess_text(text))
    return text_data

def create_lda_model(text_data, num_topics):
    # Create a Gensim dictionary
    dictionary = gensim.corpora.Dictionary(text_data)
    # Convert the text data into a bag-of-words corpus
    corpus = [dictionary.doc2bow(doc) for doc in text_data]
    # Create a Gensim LDA model
    lda_model = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, passes=15, num_topics=num_topics)
    return lda_model, dictionary

def save_lda_model(lda_model, file_name):
    file_path = os.path.join(MODELS_DIR, file_name)
    lda_model.save(file_path)

def load_lda_model(file_name):
    file_path = os.path.join(MODELS_DIR, file_name)
    return gensim.models.LdaModel.load(file_path)

def get_topic_words(lda_model, num_words):
    # Get the top words for each topic
    topic_words = []
    for topic in lda_model.print_topics(num_words=num_words):
        topic_words.append(topic[1].split("+"))
    return topic_words

def get_topic_distribution(lda_model, dictionary, text):
    # Preprocess the text
    tokens = preprocess_text(text)
    # Convert the text to a bag-of-words representation
    bow = dictionary.doc2bow(tokens)
    # Get the topic distribution for the text
    topic_distribution = lda_model.get_document_topics(bow)
    return topic_distribution

def main():
    # Load the data from the files in src/data
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    text_data = load_data(data_dir)
    # Perform topic modeling
    num_topics = 5
    lda_model, dictionary = create_lda_model(text_data, num_topics)
    # Get the top words for each topic
    num_words = 4
    topic_words = get_topic_words(lda_model, num_words)
    # Print the topic words
    for i, topic in enumerate(topic_words):
        print(f"Topic {i+1}: {topic}")

if __name__ == "__main__":
    main()

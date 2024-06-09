# src/tests/test_topic_modeling.py

import os
import sys
import gensim

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modules')))

from topic_modeling import preprocess_text, create_lda_model, save_lda_model, load_lda_model, get_topic_distribution

def test_topic_modeling():
    # Test case 1: Preprocess text
    text = "This is a sample text for testing."
    tokens = preprocess_text(text)
    assert isinstance(tokens, list)
    assert len(tokens) > 0

    # Test case 2: Create and save LDA model
    text_data = [["this", "is", "a", "sample", "document"], ["another", "sample", "document"]]
    num_topics = 2
    lda_model, dictionary = create_lda_model(text_data, num_topics)
    assert isinstance(lda_model, gensim.models.ldamodel.LdaModel)
    assert isinstance(dictionary, gensim.corpora.dictionary.Dictionary)
    
    # Save the LDA model
    save_lda_model(lda_model, "lda_model.pkl")

    # Test case 3: Load LDA model
    loaded_lda_model = load_lda_model("lda_model.pkl")
    assert isinstance(loaded_lda_model, gensim.models.ldamodel.LdaModel)

    # Test case 4: Get topic distribution
    text = "This is another sample text for testing."
    topic_distribution = get_topic_distribution(loaded_lda_model, dictionary, text)
    assert isinstance(topic_distribution, list)
    assert len(topic_distribution) > 0

    print("All tests passed!")

if __name__ == "__main__":
    test_topic_modeling()

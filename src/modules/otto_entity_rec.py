# src/modules/otto_entity_rec.py
import stanza

# Download the English model
stanza.download('en')

# Load the English pipeline
nlp = stanza.Pipeline('en')

# Define a function to perform entity recognition
def recognize_entities(text):
    # Process the text with Stanza
    doc = nlp(text)
    
    # Extract entities
    entities = []
    for ent in doc.entities:
        if ent.type == 'PERSON':
            entities.append(ent.text)
    
    return entities

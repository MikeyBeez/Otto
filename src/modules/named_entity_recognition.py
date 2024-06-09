# src/modules/named_entity_recognition.py

import spacy
from spacy import displacy

def load_nlp_model(model_name="en_core_web_sm"):
    return spacy.load(model_name)

def recognize_entities(text, nlp):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def explain_entity(entity_label):
    return spacy.explain(entity_label)

def render_entities(doc, style="ent", jupyter=True):
    displacy.render(doc, style=style, jupyter=jupyter)

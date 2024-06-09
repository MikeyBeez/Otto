import spacy
from pydantic import BaseModel
import sys
from .otto_entity_rec import recognize_entities, EntityTuple

class EntityTuple(BaseModel):
    entity_type: str
    entity_value: str

nlp = spacy.load("en_core_web_trf")

def recognize_entities(text, entity_type):
    doc = nlp(text)
    entities = [EntityTuple(entity_type=entity.label_, entity_value=entity.text) for entity in doc.ents if entity.label_ == entity_type]
    return entities

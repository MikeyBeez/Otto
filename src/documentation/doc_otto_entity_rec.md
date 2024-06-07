Here's the documentation for the otto_entity_rec.py module:
Module: otto_entity_rec.py
Description: This module performs entity recognition using the Stanza library, specifically identifying person entities in text.
Functions:
recognize_entities(text): Performs entity recognition on the input text, returning a list of person entities.
Usage:
Import the module: from src.modules import otto_entity_rec
Call the recognize_entities function with a text string: entities = otto_entity_rec.recognize_entities("John Smith is a great guy.")
Returns:
A list of person entities extracted from the text.
Example:
Input: "John Smith is a great guy."
Output: ["John Smith"]
Note:
This module uses the Stanza library and requires the English model to be downloaded using stanza.download('en').
The module loads the English pipeline using stanza.Pipeline('en').
The recognize_entities function processes the text with Stanza, extracts entities, and filters for person entities (type PERSON).

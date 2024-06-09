import unittest
import sys
sys.path.append('../modules')  # Add the modules directory to the Python path
from otto_entity_rec import recognize_entities, EntityTuple
from otto_entity_rec import recognize_entities, EntityTuple

class TestOttoEntityRec(unittest.TestCase):
    def test_recognize_entities(self):
        text = "Barack Obama was the 44th President of the United States."
        entities = recognize_entities(text, "PERSON")
        self.assertEqual(entities, [EntityTuple(entity_type='PERSON', entity_value='Barack Obama')])

if __name__ == '__main__':
    unittest.main()

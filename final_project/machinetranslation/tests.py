import unittest
from translator import english_to_french, french_to_english

class TranslatorTest(unittest.TestCase):
    def test_english_to_french(self):
        self.assertIsNotNone(english_to_french("Hello"))
        self.assertEqual(english_to_french("Hello")['translations'][0]['translation'], "Bonjour")

    def test_french_to_english(self):
        self.assertIsNotNone(french_to_english("Hello"))
        self.assertEqual(french_to_english("Bonjour")['translations'][0]['translation'], "Hello")

if __name__ == '__main__':
    unittest.main()
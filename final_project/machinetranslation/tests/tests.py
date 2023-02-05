import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_en2fr(self):
        self.assertEqual(englishToFrench(None), None)
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_fr2en(self):
        self.assertEqual(frenchToEnglish(None), None)
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    

if __name__=="__main__":
    unittest.main()


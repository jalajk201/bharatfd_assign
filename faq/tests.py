from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    def test_translation_fallback(self):
        translated_faq = self.faq.get_translated('fr')
        self.assertEqual(translated_faq["question"], "What is Django?")

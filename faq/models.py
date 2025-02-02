from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

LANGUAGES = ['hi', 'bn']  # Add more languages as needed

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Multi-language fields
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        for lang in LANGUAGES:
            if not getattr(self, f'question_{lang}'):
                setattr(self, f'question_{lang}', translator.translate(self.question, dest=lang).text)
            if not getattr(self, f'answer_{lang}'):
                setattr(self, f'answer_{lang}', translator.translate(self.answer, dest=lang).text)

        super().save(*args, **kwargs)

    def get_translated(self, lang='en'):
        cache_key = f'faq_{self.id}_{lang}'
        cached_faq = cache.get(cache_key)
        if cached_faq:
            return cached_faq

        translated = {
            "id": self.id,
            "question": getattr(self, f'question_{lang}', self.question),
            "answer": getattr(self, f'answer_{lang}', self.answer),
        }
        cache.set(cache_key, translated, timeout=3600)  # Cache for 1 hour
        return translated

    def __str__(self):
        return self.question[:50]


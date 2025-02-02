from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.all()

    def list(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')
        faqs = self.get_queryset()
        return Response([faq.get_translated(lang) for faq in faqs])

# Create your views here.

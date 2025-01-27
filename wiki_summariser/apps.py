from django.apps import AppConfig
from django.conf import settings
from transformers import pipeline

class WikiSummariserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wiki_summariser"

    def ready(self):
        if settings.configured:
            try:
                global summarizer
                summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                print("summarization model loaded succefully.")
            except Exception as e:
                print(f"Error loading summarization model: {e}")
                #global summarizer
                summarizer = None
        else:
            print("settings not configured yet. Skipping model loading.")

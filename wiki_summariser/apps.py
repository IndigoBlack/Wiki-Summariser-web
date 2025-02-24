from django.conf import settings
from django.apps import AppConfig
from transformers import pipeline

class WikiSummariserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wiki_summariser"

    def ready(self):
        if settings.configured:
            global summarizer

            try:
                print("About to initialize Summarizer")  # Debug print
                summarizer = pipeline("summarization", model="google/pegasus-xsum")
                print("Summarizer initialized")
                
            except Exception as e:
                print(f"Error loading summarization model: {e}")
                summarizer = None

            print(f"Summarizer model is: {summarizer}")  # Confirm if the model is loaded
        else:
            print("settings not configured yet. Skipping model loading.")

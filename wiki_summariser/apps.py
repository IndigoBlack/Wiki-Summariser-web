from django.apps import AppConfig
from django.conf import settings
from django.core.cache import cache
from transformers import pipeline

class WikiSummariserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wiki_summariser"

    def ready(self):
        if settings.configured:
            summarizer = cache.get('summarizer')  # Try to get from cache
            if summarizer is None:  # If not in cache, load and store
                try:
                    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                    cache.set('summarizer', summarizer, timeout=None)  # No timeout (cache indefinitely)
                    print("Summarization model loaded successfully.")
                except Exception as e:
                    print(f"Error loading summarization model: {e}")
                    summarizer = None
                    cache.set('summarizer', None, timeout=None) # Store None in cache to prevent repeated attempts
            else:
                print("Summarization model loaded from cache.")
            global summarizer
        else:
            print("settings not configured yet. Skipping model loading.")

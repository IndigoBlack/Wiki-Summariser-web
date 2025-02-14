from django.apps import AppConfig
from django.conf import settings
from django.core.cache import cache
from summarizer import Summarizer

class WikiSummariserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wiki_summariser"

    def ready(self):
        if settings.configured:
            global summarizer
            summarizer_model = cache.get('summarizer_model')
            if summarizer_model is None:
                try:
                    summarizer_model = Summarizer()
                    cache.set('summarizer_model', summarizer_model, timeout=None)
                    print("Summarization model loaded successfully.")
                except Exception as e:
                    print(f"Error loading summarization model: {e}")
                    summarizer_model = None
                    cache.set('summarizer_model', None, timeout=None)
            else:
                print("Summarization model loaded from cache.")

            summarizer = summarizer_model  # Assign the model to the global variable

        else:
            print("settings not configured yet. Skipping model loading.")
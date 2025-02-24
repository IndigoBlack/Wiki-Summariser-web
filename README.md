# In A Nutshell - Wikipedia Article Summarizer

This is a Django web application that allows users to search for Wikipedia articles on a topic of their choice. Once an article is selected, the application fetches the introductory section (overview) of the article and summarizes it using a Hugging Face Transformers model (specifically, a summarization pipeline). The user is then presented with the summarized text along with a link to the full Wikipedia page.

## Features

- Search Wikipedia articles by topic.
- Choose an article from the search results.
- Summarize the introductory section (overview) of the chosen article using a Hugging Face Transformers summarization model(google/pegasus-xsum).
- Display the summarized text along with a link to the full article.

## Requirements

- Python 3.7+ (Recommended for Transformers compatibility)
- Django 3.x or later (5.x recommended)
- `requests`
- `transformers`
- `torch` (PyTorch, required by Transformers)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/IndigoBlack/Wiki-Summariser-web](https://github.com/IndigoBlack/Wiki-Summariser-web)
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv  # On Linux/macOS
    python -m venv venv   # On Windows
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a Django project and app (if not already done):**

    ```bash
    django-admin startproject your_project_name
    cd your_project_name
    python manage.py startapp wiki_summariser
    ```

5.  **Configure Django:**
    *   Add `wiki_summariser` to `INSTALLED_APPS` in `In_a_nutshell/settings.py`.
    *   Set up your templates, URLs, and views as needed.

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```


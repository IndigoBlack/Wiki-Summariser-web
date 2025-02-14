from django.shortcuts import render
from .apps import summarizer
import requests
# Create your views here.


"""A programe that searches for an article on wikipedia for the topic the user typed in and then
    summarizes the overview of the article using an AI API then prints the link to the full article at the end."""

""" Project Title: In A Nutshell """


# Use environment variable for API key

def main(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        result = wiki_search(topic)
        if result:
            # Render the results in a template
            return render(request, "search_results.html", {"results": result, "topic": topic})
    return render(request, "search_form.html")

#Parse the user-input into the wikisearch API
def wiki_search(s):
    link = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": s,
    }
    wiki = requests.get(link, params=parameters)
    #Check if the request was successful
    if wiki.status_code == 200:
        data = wiki.json()
        search = data["query"]["search"]
        return search
    return None


def choose_article(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        choice = int(request.POST.get("choice"))
        results = wiki_search(topic)
        if results and 0 < choice <= len(results):
            article_title = results[choice - 1]["title"]
            article_content = choose_article_content(article_title)
            summarized_content = summarize(article_content)
            article_link = f"https://en.wikipedia.org/wiki/{article_title.replace(' ', '_')}"
            return render(request, "result.html", {
                "summary": summarized_content,
                "link": article_link
            })
    return render(request, "search_results.html")

def choose_article_content(title):
    link = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": title,
        "explaintext": True,
        "exintro": True,
    }
    response = requests.get(link, params=parameters)
    if response.status_code == 200:
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))
        return page.get("extract", "")
    return ""


#Use the AI API to summarize the article
def summarize(content):
    if not content:
        return "No content to summarize."
    if summarizer is None:
        return "Summarization model not loaded."
    try:
        summary = summarizer(content, max_length=150)[0]["summary_text"]
        return summary
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    main()

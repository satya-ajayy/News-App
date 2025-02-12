import requests
from datetime import datetime
import calendar
import pytz
from flask import Flask, render_template, request

app = Flask(__name__)
HTML = 'index.html'

def filterArticles(articles):
    required_keys = {"title", "author", "publishedAt", "urlToImage", "description", "url", "source"}

    filtered_articles = [
        article for article in articles
        if all(article.get(key) not in [None, ""] for key in required_keys)
        and isinstance(article.get("source"), dict)
        and article["source"].get("name") not in [None, ""]
        # and article["source"].get("id") not in [None, ""]
    ]

    return filtered_articles


def getLastMonthDate(return_str=True):
    ist = pytz.timezone("Asia/Kolkata")
    today = datetime.now(ist)
    year, month = today.year, today.month

    if month == 1:
        year -= 1
        month = 12
    else:
        month -= 1

    last_day = calendar.monthrange(year, month)[1]
    day = min(today.day, last_day)
    result_date = datetime(year, month, day, tzinfo=ist)
    return result_date.strftime("%Y-%m-%d") if return_str else result_date


def fetchNews(search, date):
    api_key = os.getenv("API_KEY")
    url = f'https://newsapi.org/v2/everything?q={search}&from={date}&sortBy=publishedAt&apiKey={api_key}'
    print(url)
    data = requests.get(url).json()
    if data['status'] == 'ok' and 'articles' in data:
        return filterArticles(data['articles'])
    else:
        return []


@app.route('/', methods=['GET'])
def homePage():
    return render_template(HTML, articles=[])


@app.route('/search', methods=['POST'])
def searchResults():
    query = request.form.get('query').lower()
    date = getLastMonthDate(return_str=True)
    return render_template(HTML, articles=fetchNews(query, date))


if __name__ == '__main__':
    app.run(debug=True)

import requests
from flask import Flask, render_template
app = Flask(__name__)


def GetNews():
    api_key = 'a6bf40d19c94490c970d85a01f6ea2d1'
    url = 'https://newsapi.org/v2/top-headlines?country=in&apikey='+api_key
    html_data = requests.get(url)
    json_data = html_data.json()
    articles = json_data['articles']
    data = []
    for article in articles:
        if article['description'] is not None:
            data.append(article)
    print(data)
    return data


# @app.route('/')
# def StartPage():
#     return render_template('StartPage.html')


@app.route('/')
def Home():
    return render_template('NewsPage.html', news_data=GetNews())


if __name__ == '__main__':
    app.run(host='0.0.0.0')

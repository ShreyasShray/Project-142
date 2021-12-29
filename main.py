from flask import Flask, jsonify, request
import csv

all_articles = []
liked_articles = []
not_liked_articles = []

with open("articles.csv") as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    articles = all_articles
    all_articles_dict = []
    for data in articles:
        _d = {
            "id":data[0],
            "index":data[1],
            "timestamp":data[2],
            "eventType":data[3],
            "contentId":data[4],
            "authorPersonId":data[5],
            "authorSessionId":data[6],
            "authorUserAgent":data[7],
            "authorRegion":data[8],
            "authorCountry":data[9],
            "contentType":data[10],
            "url":data[11],
            "title":data[12],
            "text":data[13],
            "lang,total_views":data[14],
            "total_likes":data[15],
            "total_bookmarks":data[16],
            "total_follows":data[17],
            "total_comment":data[18],
            "total_events":data[19],
        }
        all_articles_dict.append(_d)

    article = all_articles_dict[0]
    return jsonify({
        "data":article,
        "status":"success"
    }), 200

@app.route("/liked-article", methods = ["POST"])
def liked_article():
    articles = all_articles
    all_articles_dict = []
    for data in articles:
        _d = {
            "id":data[0],
            "index":data[1],
            "timestamp":data[2],
            "eventType":data[3],
            "contentId":data[4],
            "authorPersonId":data[5],
            "authorSessionId":data[6],
            "authorUserAgent":data[7],
            "authorRegion":data[8],
            "authorCountry":data[9],
            "contentType":data[10],
            "url":data[11],
            "title":data[12],
            "text":data[13],
            "lang,total_views":data[14],
            "total_likes":data[15],
            "total_bookmarks":data[16],
            "total_follows":data[17],
            "total_comment":data[18],
            "total_events":data[19],
        }
        all_articles_dict.append(_d)

    article = all_articles_dict[0]
    liked_articles.append(article)
    all_articles_dict = all_articles_dict[1:]
    return jsonify({
        "status":"success"
    }), 200

    
@app.route("/not-liked-article", methods = ["POST"])
def not_liked_article():
    articles = all_articles
    all_articles_dict = []
    for data in articles:
        _d = {
            "id":data[0],
            "index":data[1],
            "timestamp":data[2],
            "eventType":data[3],
            "contentId":data[4],
            "authorPersonId":data[5],
            "authorSessionId":data[6],
            "authorUserAgent":data[7],
            "authorRegion":data[8],
            "authorCountry":data[9],
            "contentType":data[10],
            "url":data[11],
            "title":data[12],
            "text":data[13],
            "lang,total_views":data[14],
            "total_likes":data[15],
            "total_bookmarks":data[16],
            "total_follows":data[17],
            "total_comment":data[18],
            "total_events":data[19],
        }
        all_articles_dict.append(_d)

    article = all_articles_dict[0]
    not_liked_articles.append(article)
    all_articles_dict = all_articles_dict[1:]
    return jsonify({
        "status":"success"
    }), 200

if (__name__ == "__main__"):
    app.run(debug = True)
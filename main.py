from flask import Flask, jsonify, request
import csv
from storage import all_articles 
from storage import liked_articles 
from storage import not_liked_articles 
from demographic_filtering import output
from content_filtering import get_recommendation
from content_filtering import cosine_sim2

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

@app.route("/popular-article")
def pop_article():
    article = output[0]
    _d = {
        "id":article[0],
        "index":article[1],
        "timestamp":article[2],
        "eventType":article[3],
        "contentId":article[4],
        "authorPersonId":article[5],
        "authorSessionId":article[6],
        "authorUserAgent":article[7],
        "authorRegion":article[8],
        "authorCountry":article[9],
        "contentType":article[10],
        "url":article[11],
        "title":article[12],
        "text":article[13],
        "lang":article[14],
        "total_views":article[15],
        "total_likes":article[16],
        "total_bookmarks":article[17],
        "total_follows":article[18],
        "total_comment":article[19],
        "total_events":article[20],
    }
    return jsonify({
        "data":_d,
        "status":"success"
    })

@app.route("/recommended-article")
def recommended_article():
    all_recommended = []
    for lik_article in liked_articles:
        output = get_recommendation(lik_article["title"], cosine_sim2)
        for data in output:
            all_recommended.append(data)
    return jsonify({
        "data":all_recommended,
        "status":"success"
    })

if (__name__ == "__main__"):
    app.run(debug = True)
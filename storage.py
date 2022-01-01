import csv
all_articles = []
liked_articles = []
not_liked_articles = []

with open("articles.csv") as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_articles = data[1:]
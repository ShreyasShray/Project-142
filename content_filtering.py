import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("articles.csv")

count = CountVectorizer(stop_words = "english")
count_metrics = count.fit_transform(df["title"])

cosine_sim2 = cosine_similarity(count_metrics, count_metrics)

df = df.reset_index()
indices = pd.Series(df.index, index = df["title"])

def get_recommendation(title, cosine_sim):
  idx = indices[title]
  sim_score = list(enumerate(cosine_sim[idx]))
  sim_score = sorted(sim_score, key = lambda x:x[1], reverse = True)
  sim_score = sim_score[1:11]
  content_indices = [i[0] for i in sim_score]
  return df["title"].iloc[content_indices]
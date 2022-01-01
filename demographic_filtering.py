import numpy as np
import pandas as pd

df = pd.read_csv("articles.csv")

all_articles_sorted = df.sort_values("total_events", ascending = False)
output = all_articles_sorted.head(20).values.tolist()
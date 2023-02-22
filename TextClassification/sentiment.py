import pandas as pd
from snownlp import SnowNLP
df = pd.read_csv("./resources/cropus/comments.csv")

def get_sentiment_cn(text):
    s = SnowNLP(text)
    return s.sentiments

df["sentiment"] = df.comments.apply(get_sentiment_cn)

ata1=df.to_csv('./sentiments.csv')
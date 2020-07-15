# -*- coding: utf-8 -*-
"""EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nWfOrKWb5nOMsorkA0rJyKRwDO8pZi5e
"""

from google.colab import drive
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

drive.mount('/content/drive')
df=pd.read_csv('/content/drive/My Drive/IBM/tweets_raw.csv',index_col = None)

def detect_polarity(text):
    return TextBlob(text).sentiment.polarity
df['polarity'] = df.tweet.apply(detect_polarity)
df_polarity = df[['tweet','polarity']]
df_polarity.describe()

fig, ax = plt.subplots(figsize=(10, 7))

# Plot histogram of the polarity values
df_polarity.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
             ax=ax,
             color="black")

plt.xlabel("Polarity")
plt.ylabel("Number of TImes")
plt.title("Sentiments from Tweets ")
plt.show()

df=pd.read_csv('/content/drive/My Drive/IBM/tweets_preprocessed_final_pakka_promise.csv',index_col = None)

def detect_polarity(text):
    return TextBlob(text).sentiment.polarity
df['polarity'] = df.tweet.apply(detect_polarity)
df_polarity = df[['tweet','polarity']]
df_polarity.describe()

fig, ax = plt.subplots(figsize=(10, 7))

# Plot histogram of the polarity values
df_polarity.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
             ax=ax,
             color="black")

plt.xlabel("Polarity")
plt.ylabel("Number of TImes")
plt.title("Sentiments from Tweets ")
plt.show()
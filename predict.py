from newspaper import Article
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import numpy as np
import itertools
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='7d125ba012bc447681da91239d255267')
linear_clf = pickle.load(open("model.pickle", "rb"))

tfidf_vectorizer = pickle.load(open("vectorizer.pickle", "rb"))

def predict_fake(title, text):
	data = {"Unnamed: 0": ["0000"], "title":[title], "text":[text], "label":["FAKE/REAL"]}
	frame = pd.DataFrame(data, columns = ["Unnamed: 0", "title", "text", "label"])
	frame = frame.set_index("Unnamed: 0")
	frame.drop("label", axis=1)
	tfidf_test = tfidf_vectorizer.transform(frame['text'])
	pred = linear_clf.predict(tfidf_test)
	return pred[0]

def compare(a, b):
	for i in a:
		if i.lower() in b:
			return "NOT CLICKBAIT"
	return "CLICKBAIT"


def predict(url):
	article = Article(url)
	article.download()
	article.parse()
	

	if len(article.text) <= 500:
		return [str(article.title)] + (["INVALID"] * 3)
	article.nlp()
	return [str(article.title), predict_fake(str(article.title), str(article.text)), compare(article.title.split(), article.keywords), str(article.summary)] 


def get_headlines():
	final = []
	top_headlines = newsapi.get_top_headlines(language='en')
	for i in top_headlines['articles']:
		final.append(i['url'])
	return final

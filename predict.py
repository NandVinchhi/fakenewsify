import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import numpy as np
import itertools
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle

linear_clf = pickle.load(open("model.pickle", "rb"))

tfidf_vectorizer = pickle.load(open("vectorizer.pickle", "rb"))

def predict(title, text):
	data = {"Unnamed: 0": ["0000"], "title":[title], "text":[text], "label":["FAKE/REAL"]}
	frame = pd.DataFrame(data, columns = ["Unnamed: 0", "title", "text", "label"])
	frame = frame.set_index("Unnamed: 0")
	frame.drop("label", axis=1)
	tfidf_test = tfidf_vectorizer.transform(frame['text'])
	pred = linear_clf.predict(tfidf_test)
	return pred[0]


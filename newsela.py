import textblob
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score

import json
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from sklearn import svm


def get_ngrams(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return [' '.join(grams) for grams in n_grams]



def main():
    file_path = "C:\\Users\\ravis\\Desktop\\newsela\\quiz_questions.json"
    f = open(file_path)
    quiz_question_file = json.load(f)
    i = 0
    n = 3
    while i < 10:
        i += 1
        print(quiz_question_file[i]["percent_correct"])
        sentence = quiz_question_file[i]["percent_correct"]
        trigrams = ngrams(sentence.split(), n)
        print(trigrams)
    classifier = svm.LinearSVC(C=1.0, class_weight="balanced")
#!/usr/bin/env python3

"""
Do Term Frequency - Inverse Document Frequency analysis of the Ofsted reports
@args: None
@instructions: see ..poppins for usage
"""


#-- Imports ---------------------------------------------------------------------
# base #
import json
import string

# third party #
import nltk
import pandas as pd

from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

#-- Variables -------------------------------------------------------------------
token_dict = {
    'outstanding': {},
    'good': {},
    'improve': {},
    'inadequate': {}
}

output = {
    'outstanding': {},
    'good': {},
    'improve': {},
    'inadequate': {}
}

stemmer = PorterStemmer()


#-- Functions -------------------------------------------------------------------
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

def go(grouping, df):
    """
    Do the tf-idf analysis of each of the columns within the rating
    """
    for column in df.columns[3:]:
        text = [str(i).lower() for i in df[column]]
        removals = str.maketrans("", "", string.punctuation)

        text = [i.translate(removals) for i in text]
        token_dict[grouping][column] = text


#-- Main ------------------------------------------------------------------------
def main():
    df = pd.read_csv('./data/reports.csv')
    g = df.groupby('rating')

    ## housekeeping
    for group, data in g:
        go(group, data)

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')

    for group, data in g:
        for column in data.columns[3:]:
            output[group][column] =\
              tfidf.fit_transform(token_dict[group][column])

    #+TODO: serialise the CSR and find a reasonable way to output it by
    #       reindexing to have the LA as the index rather than the current one
    #       automatically generated from the vectoriser
    #
    #       assign: @ceryshop-dsc


if __name__ == '__main__':
    main()

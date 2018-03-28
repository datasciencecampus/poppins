"""
Program to generate a word cloud per rating per section for the combined
Ofsted reports
"""


#-- Imports ---------------------------------------------------------------------

import json
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud



##-- Functions ------------------------------------------------------------------

def genCloud(df):
    """
    Create a wordcloud for every column in a dataframe
    """
    global category

    category += 1
    print(f'Processing rating {category}')
    
    section = 0
    # we don't want the first two, la and rating are meaningless here
    for key in df.columns[3:]:
        section += 1
        print(f'    .. Processing section {section}', end='\r', flush='')
        text = ''.join(str(s) for s in df[key])
        wordcloud = WordCloud().generate(text)
        ## TODO: remove casting, make it work properly
        rating = df['rating'].iloc[0]

        with open(f'../output/{rating}/scores/{key}.json','w') as file:
            json.dump(wordcloud.words_, file, indent=4)

        # set up and save the output of the wordcloud processing
        plt.figure(figsize=(16,9), dpi=133)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(f'../output/{rating}/{key}.jpg')


#-- Main ------------------------------------------------------------------------
if __name__ == '__main__':

    # some global counters
    category = 0

    reports = pd.read_csv('../data/reports.csv', dtype=str, engine='c')
    g = reports.groupby('rating')
    g.apply(genCloud)

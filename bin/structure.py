"""
Preparation of the Ofsted reports for discovery analysis
"""


#-- Imports ---------------------------------------------------------------------

import csv
import glob
import os
import pandas as pd
import re
import sqlite3


#-- Variables -------------------------------------------------------------------

# set up paths relative to this file
dirname, filename = os.path.split(os.path.abspath(__file__))
files = glob.glob(f"{dirname}/../data/*txt/*.txt")

# define split by sections
# NOTE: this will result in 7 sections and the first is the stuff before the
#       Executive summary
sections = [i.strip('\n') for i in open('etc/sections.txt').readlines()]

# short names for the sections to be used in csv output
short = [i.strip(' \n') for i in open('etc/short.txt').readlines()]

records = []


#-- Main ------------------------------------------------------------------------

if __name__ == '__main__':

    counter = 0
    for file in files:
        # NOTE:
        #   there are 129 files
        #   >  find data -name '*.txt' | wc -l
        #   129
        with open(file, 'r') as text_file:
            counter += 1
            # split out the path name into
            rating, la = os.path.split(file)

            # tidy up the values above
            rating = os.path.split(rating)[1][:-4]
            la = re.sub(r'(.*?)_.*.txt', r'\1', la)

            # time to set up the data and push it to our list
            text = text_file.read().replace('\n', ' ')
            split_text = []

            split_text.append(la)
            split_text.append(rating)

            for j in range(len(sections)):
                split_text.append(text.split(sections[j], 1)[0])
                text = text.split(sections[j], 1)[-1]

            split_text.append(text.split(sections[j], 1)[-1])

            records.append(split_text)
        print(f'    .. Processed {counter} files', end='\r', flush='')


    df = pd.DataFrame(records, columns = short)

    df.to_csv('data/reports.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)


    #output the thing to an SQLite3 database as well (no harm)
    con = sqlite3.connect('data/ofsted.db')
    df.to_sql('reports', con, if_exists='replace')

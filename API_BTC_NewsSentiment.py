#connecting to newsAPI
#while using textblob for NLP sentiment analysis

#reqs:
# pip install newsapi-python
# pip install -U textblob  //not sure what the -U flag is meant to do..
from newsapi import NewsApiClient
import csv
import pandas as pd
from textblob import TextBlob
from dateutil import parser
api = NewsApiClient(api_key='d7be4b06f0a94595825b3137e3683ad4')


content = api.get_everything(q='bitcoin',
                             sources = 'bbc-news, metro, financial-times, cnbc, business-insider, reuters, wired, vice-news, usa-today, time, the-washington-times, the-washington-post, the-wallstreet-journaal, the-verge, the-next-web, the-huffington-post, the-hill, the-american-conservative, techradar, techcrunch, reddit-r-all, recode, polygon, politico, nfl-news, new-york-magazine, new-scientist',
                             language = 'en'
)
#print(content)
content_df = pd.DataFrame(content['articles'])
content_df
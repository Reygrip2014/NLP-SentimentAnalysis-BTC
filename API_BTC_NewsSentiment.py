#connecting to newsAPI
#while using textblob for NLP sentiment analysis

#reqs:
# pip install newsapi-python
# pip install -U textblob  //not sure what the -U flag is meant to do..
from newsapi import NewsApiClient
import csv
from nltk.util import Index
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


##############
# below works but need to work out more details with regards to;
#   - lamba
#   - parser for dat
#   - textblobs algorithm for subjectivity and polarity
##############

content_df['date'] = content_df.apply(lambda x: parser.parse(x['publishedAt']).strftime('%Y.%m.%d'), axis=1)
#content_df['time'] = content_df.apply(lambda x: parser.parse(x['publishedAt']).strftime('%H:%M'), axis=1)

content_df['polarity'] = content_df.apply(lambda x: TextBlob(x['description']).sentiment.polarity, axis=1)
#content_df['subjectivity'] = content_df.apply(lambda x: TextBlob(x['description']).sentiment.subjectivity, axis=1)

content_df


###############
# next steps would be to find a good weight (e.g. number of readers) to create a weigthed average of positivty scores
# and then plot it against bitcoin historical price data


#content_df.groupby('date')['polarity'].mean().plot(kind='line')
datanew = content_df.groupby(by = 'date').mean()
datanew.plot(kind='line')
plt.show()
datanew.shape
datanew.info()
import seaborn as sns
import matplotlib.pyplot as plt
#ax = plt.gca()
plt.show()

#plotten gaat fout omdat 'date' niet echt in de df zit als kolomnaam
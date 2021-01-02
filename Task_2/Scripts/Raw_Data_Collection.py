# Anuneet Anand
# 2018022
# Raw Tweet Collection

import json
import tweepy
import pandas as pd

# Authentication : Add Your Keys!

consumer_key = ''
consumer_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Collecting Top 10 Trending Hashtags in Delhi

woeid_Delhi = 20070458
result = api.trends_place(id = woeid_Delhi)
trends = pd.DataFrame(result[0]['trends'])[['name','tweet_volume']]
trends = trends[trends.name.str.contains('#')]
trends.dropna(inplace=True)
trends.reset_index(inplace=True,drop=True)

df = pd.DataFrame()
df['Hashtag'] = trends['name']
df['Tweet_Volume'] = trends['tweet_volume'].astype(int)
df.sort_values(inplace=True,axis=0,by=['Tweet_Volume'],ascending=False,ignore_index=True)
df = df[:10]

df.to_json('../Dump/Top_HashTags.json')

# Collecting 10000 Tweets & Retweets with given HashTag near Delhi

Query = '#HappyNewYear'
Geo_Delhi = '28.7041,77.1025,250km'
cursor = tweepy.Cursor(api.search,q = Query,  geocode = Geo_Delhi,tweet_mode = "extended").items(10000)

Raw_Tweets = []
for i in cursor:
	x = i._json
	if 'retweeted_status' in x:
		x['text']=x['retweeted_status']['full_text']
		del x['retweeted_status']
		del x['full_text']
	else:
		x['text']=x['full_text']
		del x['full_text']
	Raw_Tweets.append(json.dumps(x))

with open('../Dump/Raw_Tweets.json','w') as file:
	for i in Raw_Tweets:
		file.write(i+"\n")
file.close()

# END OF CODE

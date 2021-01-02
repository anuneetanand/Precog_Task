# Anuneet Anand
# 2018022
# Cleaning Tweets

import json
import pandas as pd

# Extracting relevant data from json dump

Tweets = pd.DataFrame(columns=['id','user_id','created_at','lang','retweet_count', 'favorite_count','source','hashtags','symbols','text'])
Users = pd.DataFrame(columns=['id', 'name', 'screen_name','created_at','location','protected','followers_count','friends_count','favourites_count','verified'])

Tweet_Attributes =  ['created_at','id','text', 'source', 'retweet_count', 'favorite_count','lang']
User_Attributes = ['id', 'name', 'screen_name', 'location','protected','followers_count','friends_count','favourites_count','created_at','verified']

with open('../Dump/Raw_Tweets.json','r') as file:
	Data = file.readlines()

	for x in range(len(Data)):
		D = json.loads(Data[x])

		T = {}
		U = {}

		for i in Tweet_Attributes:

			if i == 'source' and len(D[i]):
				T[i]= D[i].split(">")[1][:-3]
			else:
				T[i]=D[i]

		T['user_id'] = D['user']['id']
		H = []
		for i in D['entities']['hashtags']:
			H.append(i['text'])
		T['hashtags']=H

		for i in User_Attributes:
			U[i]=D['user'][i]

		Tweets = Tweets.append(T,ignore_index=True)
		Users = Users.append(U,ignore_index=True)

Tweets.to_json('../Dump/Tweets.json')
Users.to_json('../Dump/Users.json')

# END OF CODE

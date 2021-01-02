# Anuneet Anand
# 2018022
# Web App

import io
import re
import json
import dash
import base64
import pandas as pd
import textblob as tb
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output


# Reading DataFrames
Tweets = pd.read_json('Dump/Tweets.json')
Users = pd.read_json('Dump/Users.json')


Activity = {i:0 for i in range(24)}
for i in Tweets['created_at']:
    Activity[int(str(i)[11:13])]+=1
x = [str(i) for i in Activity]
y = [Activity[i] for i in Activity]
df = pd.DataFrame()
df['x'] = x
df['y'] = y
Fig_A = px.bar(df, x="x",y='y',labels={"x": "Hour of Day","y": "Tweet Volumne"})


df = Tweets
Tweet_Texts = df[df.lang.str.contains('en')]['text'] 
Positive = 0
Negative = 0
Neutral = 0
for T in Tweet_Texts:
    Cleaned_Text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", T).split())
    Result = tb.TextBlob(Cleaned_Text).sentiment.polarity
    if Result > 0: Positive+=1
    elif Result < 0: Negative+=1
    else: Neutral+=1
labels = ["Neutral","Positive","Negative"]
values = [Neutral,Positive,Negative]
Fig_B = go.Figure(data=[go.Pie(labels=labels, values=values)])


df = Tweets
labels = ["Android","Desktop","iPhone","Other"]
sizes = []
sizes.append(len(df[df['source'].str.contains('Twitter for Android')]))
sizes.append(len(df[df['source'].str.contains('Twitter Web App')]))
sizes.append(len(df[df['source'].str.contains('Twitter for iPhone')]))
sizes.append(len(df)-sum(sizes))
Fig_C = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.5)])


df = Tweets
df = df.lang.value_counts().to_frame().reset_index() 
df.columns = ['Language','Tweets']
df = df.sort_values(['Tweets'],ascending=False)
df = df.append({'Language':'other', 'Tweets': df[3:]['Tweets'].sum()},ignore_index=True)
df = df.sort_values(['Tweets'],ascending=False)
df = df[:4]
Fig_D = go.Figure(data=[go.Pie(labels=['English','Hindi','Unknown','Other'], values=list(df['Tweets']), hole=.5)])


df = Users
Followers = list(df['followers_count'])
D = {'0-250':0,'251-1000':0,'1001-2500':0,'2501-10000':0,'>10000':0}
for i in Followers:
    if i<=250:D['0-250']+=1
    elif i<=1000:D['251-1000']+=1
    elif i<=2500:D['1001-2500']+=1
    elif i<=10000:D['2501-10000']+=1
    else:D['>10000']+=1
x = [i for i in D]
y = [D[i] for i in D]
df = pd.DataFrame()
df['x'] = x
df['y'] = y
Fig_E = px.bar(df, x="x",y='y',labels={"x": "Followers","y": "No. Of Users"})


df = Users
Friends = list(df['friends_count'])
D = {'0-250':0,'251-1000':0,'1001-2500':0,'2501-10000':0,'>10000':0}
for i in Friends:
    if i<=250:D['0-250']+=1
    elif i<=1000:D['251-1000']+=1
    elif i<=2500:D['1001-2500']+=1
    elif i<=10000:D['2501-10000']+=1
    else:D['>10000']+=1
x = [i for i in D]
y = [D[i] for i in D]
df = pd.DataFrame()
df['x'] = x
df['y'] = y
Fig_F = px.bar(df, x="x",y='y',labels={"x": "Friends","y": "No. Of Users"})


# DASH APP

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    
    html.H1("Twishigo",style = {'text-align': 'center'}),
    html.H2("Trending : #HappyNewYear",style = {'text-align': 'center'}),
    
    html.Img(src='data:WordCloud_Tweets/png;base64,{}'.format(base64.b64encode(open('./WordCloud_Tweets.png', 'rb').read()).decode('ascii'))),
    
    html.H2("Number Of Tweets Vs. Hour of Day",style = {'text-align': 'center'}),
    html.Div([core.Graph(id = "A",figure = Fig_A ,style={'display': 'block', 'width': '1000px','margin-left':'auto','margin-right':'auto'})]),

    html.H2("Sentiment Analysis",style = {'text-align': 'center'}),
    html.Div([core.Graph(id = "B",figure = Fig_B ,style={'display': 'block', 'width': '1000px','margin-left':'auto','margin-right':'auto'})]),

    html.H2("Tweeting Platforms",style = {'text-align': 'center'}),
    html.Div([core.Graph(id = "C",figure = Fig_C ,style={'display': 'block', 'width': '1000px','margin-left':'auto','margin-right':'auto'})]),

    html.H2("Languges In Tweets",style = {'text-align': 'center'}),
    html.Div([core.Graph(id = "D",figure = Fig_D ,style={'display': 'block', 'width': '1000px','margin-left':'auto','margin-right':'auto'})]),

    html.H2("Distribution of Friends",style = {'text-align': 'center'}),
    html.Div([core.Graph(id = "E",figure = Fig_E ,style={'display': 'block', 'width': '1000px','margin-left':'auto','margin-right':'auto'})]),

    html.H2("Distribution of Followers",style = {'text-align': 'center'}),
    html.Div([core.Graph(id = "F",figure = Fig_F ,style={'display': 'block', 'width': '1000px','margin-left':'auto','margin-right':'auto'})])])

if __name__ == '__main__':
    app.run_server(debug=True,port=5001)

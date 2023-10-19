import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)
init_notebook_mode(connected=True)

st.header("Data Visualization of Spotify")

st.markdown(''' Spotify transformed music listening forever when it launched in Sweden in 2008. Discover, 
manage and share over 70m tracks for free, or upgrade to Spotify Premium to access exclusive features including
offline mode, improved sound quality, and an ad-free music listening experience.
Today, Spotify is the most popular global audio streaming service with 365m users, 
including 165m subscribers across 178 markets. 
They are the largest driver of revenue to the music business today''')

df=pd.read_csv(r'D:\Minor project\Dataset\songs_normalize.csv')

df.head()

df.info

df.duplicated().value_counts()

df.drop_duplicates(inplace=True)

df.shape

df.describe()


# plotly graph

fig1=make_subplots(rows=3,cols=3,subplot_titles=('<i>popularity', '<i>danceability', '<i>energy', '<i>loudness', '<i>speechiness', '<i>acousticness', '<i>liveness', '<i>valence', '<i>tempo'))
fig1.add_trace(go.Histogram(x=df['popularity'],name='popularity'),row=1,col=1)
fig1.add_trace(go.Histogram(x=df['danceability'],name='danceability'),row=1,col=2)
fig1.add_trace(go.Histogram(x=df['energy'],name='energy'),row=1,col=3)
fig1.add_trace(go.Histogram(x=df['loudness'],name='loudness'),row=2,col=1)
fig1.add_trace(go.Histogram(x=df['speechiness'],name='speechiness'),row=2,col=2)
fig1.add_trace(go.Histogram(x=df['acousticness'],name='acousticness'),row=2,col=3)
fig1.add_trace(go.Histogram(x=df['liveness'],name='liveness'),row=3,col=1)
fig1.add_trace(go.Histogram(x=df['valence'],name='valence'),row=3,col=2)
fig1.add_trace(go.Histogram(x=df['tempo'],name='tempo'),row=3,col=3)
fig1.update_layout(height=900,width=900,title_text='<b>Feature Distribution')
fig1.update_layout(template='plotly_dark',title_x=0.5)
st.plotly_chart(fig1)

st.markdown('<h3 style="font-weight:bold; color:red">Data visuatlization on area graph</h3>', unsafe_allow_html=True)
fig2=px.area(df.groupby('year',as_index=False).count().sort_values(by='song',ascending=False).sort_values(by='year'),x='year',y='song',markers=True,labels={'song':'Total songs'},color_discrete_sequence=['green'],title='<b>Year by Year Songs collection')
fig2.update_layout(hovermode='x',title_x=0.5)
st.plotly_chart(fig2)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization on histogram graph</h3>', unsafe_allow_html=True)
fig3=px.histogram(df.groupby('genre',as_index=False).count().sort_values(by='song',ascending=False),x='genre',y='song',color_discrete_sequence=['green'],template='plotly_dark',marginal='box',title='<b>Total songs based on genres</b>')
fig3.update_layout(title_x=0.5)
st.plotly_chart(fig3)

st.markdown('<h3 style="font-weight:bold&Italic; color:Blue">Data visuatlization based on Poplarity</h3>', unsafe_allow_html=True)
fig4=px.histogram(df.groupby('genre',as_index=False).sum().sort_values(by='popularity',ascending=False),x='genre',y='popularity',color_discrete_sequence=['lightgreen'],template='plotly_dark',marginal='box',title='<b>Popular genres based on pouplarity</b>')
fig4.update_layout(title_x=0.5)
st.plotly_chart(fig4)

st.markdown('<h3 style="font-weight:bold&Italic; color:Violet">Data visuatlization based on Poplarity</h3>', unsafe_allow_html=True)
fig5=px.bar(df.groupby('artist',as_index=False).count().sort_values(by='song',ascending=False).head(50),x='artist',y='song',labels={'song':'Total Songs'},width=1000,color_discrete_sequence=['green'],text='song',title='<b> List of Songs Recorded by Each Singer')
st.plotly_chart(fig5)

st.markdown('<h3 style="font-weight:bold&Italic; color:Brown">Data visuatlization based on 30 Singers </h3>', unsafe_allow_html=True)
fig6=px.bar(df.groupby('artist',as_index=False).sum().sort_values(by='popularity',ascending=False).head(30),x='artist',y='popularity',color_discrete_sequence=['lightgreen'],template='plotly_dark',text='popularity',title='<b>Top 30 Popular Singers')
st.plotly_chart(fig6)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization based on 25 Singers </h3>', unsafe_allow_html=True)
fig7=px.line(df.sort_values(by='popularity',ascending=False).head(25),x='song',y='popularity',hover_data=['artist'],color_discrete_sequence=['green'],markers=True,title='<b> Top 25 songs in Spotify')
st.plotly_chart(fig7)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization based on Singers Playlist </h3>', unsafe_allow_html=True)
fig8=px.treemap(df,path=[px.Constant('Singer'),'artist','genre','song'],values='popularity',title='<b>TreeMap of Singers Playlist')
fig8.update_traces(root_color='lightgreen')
fig8.update_layout(title_x=0.5)
st.plotly_chart(fig8)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization based on Explicit Songs </h3>', unsafe_allow_html=True)
fig9=px.pie(df.groupby('explicit',as_index=False).count().sort_values(by='song',ascending=False),names='explicit',values='song',labels={'song':'Total songs'},hole=.6,color_discrete_sequence=['green','crimson'],template='plotly_dark',title='<b>Songs having explicit content')
fig9.update_layout(title_x=0.5)
st.plotly_chart(fig9)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization based on Year Wise Explicit Songs </h3>', unsafe_allow_html=True)
fig10=px.area(df[df['explicit']==True].groupby('year',as_index=False).count().sort_values(by='song',ascending=False).sort_values(by='year'),x='year',y='song',labels={'song':'Total songs'},markers=True,color_discrete_sequence=['red'],template='plotly_dark',title='<b>Yearwise explicit content songs')
fig10.update_layout(hovermode='x')
st.plotly_chart(fig10)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization based on Year Popularly Wise Explicit Songs </h3>', unsafe_allow_html=True)
fig11 = px.box(df,x='explicit',y='popularity',color='explicit',template='plotly_dark',color_discrete_sequence=['cyan','magenta'],title='<b>popularity based on explicit content')
st.plotly_chart(fig11)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization Tempo versus Popularity </h3>', unsafe_allow_html=True)
fig12=px.scatter(df,x='tempo',y='popularity',color='tempo',color_continuous_scale=px.colors.sequential.Plasma,template='plotly_dark',title='<b>Tempo Versus Popularity')
st.plotly_chart(fig12)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization Energy versus Popularity </h3>', unsafe_allow_html=True)
fig13=px.scatter(df,x='speechiness',y='popularity',color='speechiness',color_continuous_scale=px.colors.sequential.Plasma,template='plotly_dark',title='<b> Speechiness Versus Popularity')
st.plotly_chart(fig13)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization Energy versus Danceablity </h3>', unsafe_allow_html=True)
fig14=px.scatter(df,x='energy',y='danceability',color='danceability',color_continuous_scale=px.colors.sequential.Plotly3,template='plotly_dark',title='<b>Energy Versus Danceability')
st.plotly_chart(fig14)

st.markdown('<h3 style="font-weight:bold&Italic; color:Green">Data visuatlization Energy versus Loudnesscorrelation </h3>', unsafe_allow_html=True)
fig15=px.scatter(df,x='energy',y='loudness',color_discrete_sequence=['lightgreen'],template='plotly_dark',title='<b>Energy versus Loudness correlation')
st.plotly_chart(fig15)





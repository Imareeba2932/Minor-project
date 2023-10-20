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

st.markdown('<h2 style="color: maroon; text-align:center; background-color: #AEF359; font-family:Verdana; border: 3px dashed #028A0F; border-radius:5px; margin-bottom: 20px; ">SPOTIFY SONGS DATA ANALYSIS AND VISUALIZATION</h2>', unsafe_allow_html=True)

st.markdown('''<p style="font-weight:bold; font-size: 20px; font-family:Cursive"> Imagine having access to a never-ending jukebox filled with millions
             of songs, podcasts, and playlists tailored just for you. Welcome to Spotify,
             the magical realm where music meets technology. It's your passport to a world 
            of tunes that can whisk you away to far-off places, stir your emotions,
             and keep you grooving through the highs and lows of life. With Spotify, 
            you're not just listening; you're embarking on a sonic adventure where your 
            favorite melodies are just a click away. </p>''', unsafe_allow_html=True)
st.image('Assets\spot.gif', use_column_width=True)

st.markdown("About the project")
st.markdown("About the Dataset")

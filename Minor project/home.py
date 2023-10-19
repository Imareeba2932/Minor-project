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

st.title("spotify songs analysis")
st.subheader('Latest songs collection')
st.markdown(''' Spotify is a digital music, podcast, 
and video service that gives you access to millions of songs 
and other content from creators all over the world. 
Basic functions such as playing music are totally free, but you can also choose to upgrade to Spotify Premium.
''')
st.image(r'Assets\unnamed.png', use_column_width=True)

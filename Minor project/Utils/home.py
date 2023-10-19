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

st.title("CALCULATOR")
st.markdown('Welcome To My First  Streamlit App 🤣')
st.image(r'C:\Users\siddhant new ac\Desktop\new batch\Minor project\Assets\spotify-2.png')
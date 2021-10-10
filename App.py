from re import template
from PIL.Image import ROTATE_90
from plotly.express import data
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit.proto.Markdown_pb2 import Markdown
sidebar=st.sidebar
sidebar.text('Dataset')
selectoption = sidebar.selectbox('SELECT ONE',['View Data','Visualizations'])
BTN = sidebar.button('Submit')
if BTN:
    st.balloons()
    sidebar.text(f'Enjoy')
def init():
    st.title('Analytics of Spotify Hits')
    st.image('Spot.gif')
    st.subheader('Data for Spotify Hits')

init()
df = pd.read_csv('Spotify.csv')
st.dataframe(df)
df.drop( columns=['id', 'uri', 'track_href', 'analysis_url'], inplace=True )
def showdata():
    st.header('Dataset used in this project')
    st.markdown('---')
    st.dataframe(df)

def Viewanalysis():
    st.header('Visualizations')

if selectoption == 'View Data':
    showdata()
elif selectoption == 'Visualizations':
    Viewanalysis()



st.subheader('Genre - Danceability')
Songs=df.head(21524)
st.plotly_chart(px.scatter(data_frame=Songs,x='genre',y='danceability',height=800,width=1100,template = 'none',color='danceability'))
st.markdown('# ')


st.subheader('Loudenss - Genre')
Songs=df.head(42304)
st.plotly_chart(px.scatter(data_frame=Songs,x='loudness',y='genre',height=800,width=1100,color_continuous_scale=px.colors.sequential.Viridis,template = 'none',color='loudness'))
st.markdown('# ')



st.subheader('Time signature - Genre')
Songs=df.head(42304)
st.plotly_chart(px.bar(data_frame=Songs,x='genre',y='time_signature',hover_name='song_name',height=800,width=1100,template='none',color='time_signature'))
st.markdown('# ')


st.subheader('Name - Genre')
Songs=df.head(30000)
st.plotly_chart(px.scatter(data_frame =Songs, x='song_name',y='genre', color ='genre',height=800,width=1100,hover_name='song_name',template='plotly_dark'))
st.markdown('# ')


st.subheader('Liveness - Song - Tempo')
Songs=df.head(100)
st.plotly_chart(px.scatter_3d(data_frame=Songs,x='tempo',y='liveness',z='song_name',height=800,width=1100,hover_name='song_name',template='plotly_dark',color='tempo'))
st.markdown('# ')



st.subheader('Songs - Energy')
Songs=df.head(100)
st.plotly_chart(px.histogram(data_frame=Songs,x='song_name',y='energy',height=800,width=1200,template='plotly',color='energy'))
st.markdown('# ')


st.subheader('Mode - Genre')
Songs=df.head(42304)
st.plotly_chart(px.histogram(data_frame=Songs,x='mode',y='genre',template='seaborn',height=800,width=1100,color='genre'))
st.markdown('# ')


st.subheader('Key - Genre')
Songs=df.head(42304)
st.plotly_chart(px.histogram(data_frame=Songs,x='key',y='genre',template='gridon',height=800,width=1100,color='genre'))
st.markdown('# ')



st.subheader('Type - Genre')
Songs=df.head(42304)
st.plotly_chart(px.scatter_3d(data_frame=Songs,x='genre',y='type',z='song_name',template='none',color='genre'))
st.markdown('# ')


st.subheader('Type - Genre')
Songs=df.head(42304)
st.plotly_chart(px.density_heatmap(data_frame=Songs,x='genre',y='type',template='none'))
st.markdown('# ')




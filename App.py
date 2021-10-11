from re import template
from PIL.Image import ROTATE_90
from plotly.express import data
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit.proto.Markdown_pb2 import Markdown
sidebar=st.sidebar
sidebar.text('Dataset')
sidebar.image('Music.gif')
selectoption = sidebar.selectbox('SELECT ONE ✌️',['View Data','Visualizations'])

if selectoption:
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
    st.markdown('---')

if selectoption == 'View Data':
    showdata()
elif selectoption == 'Visualizations':
    Viewanalysis()


st.subheader('Genre - Danceability')
Songs=df.head(21524)
st.caption('This scatter shows us the danceability genre wise')
st.plotly_chart(px.bar(data_frame=Songs,x='genre',y='danceability',hover_name='song_name',height=800,width=1100,template = 'none',color='genre'))
st.markdown('# ')



st.subheader('Loudness - Genre')
Songs=df.head(25000)
st.caption('This scatter tells us about the loudness per genre')
st.plotly_chart(px.bar(data_frame=Songs,x='genre',y='loudness',template='none',height=800,width=1100,hover_name='song_name',color='genre'))
st.markdown('# ')



st.subheader('Time signature - Genre')
Songs=df.head(42304)
st.caption('This chart shows us the time signature to genre')
Songs=df.sort_values('time_signature',ascending=False)
st.plotly_chart(px.bar(data_frame=Songs,x='genre',y='time_signature',hover_name='song_name',height=800,width=1100,template='none',color='genre'))
st.markdown('# ')




st.subheader('Name - Genre')
Songs=df.head(30000)
st.caption('This scatter chart show us the first 30000 songs in their respective genre')
st.plotly_chart(px.scatter(data_frame =Songs, x='song_name',y='genre', color ='genre',height=800,width=1100,hover_name='song_name',template='plotly_dark'))
st.markdown('# ')



st.subheader('Liveness - Song - Tempo')
Songs=df.head(100)
st.caption('This scatter 3D chart gives us an overview of Liveness,Tempo to the first 100 songs in the dataset used')
st.plotly_chart(px.scatter_3d(data_frame=Songs,x='tempo',y='liveness',z='song_name',height=800,width=1100,hover_name='song_name',template='plotly_dark',color='tempo'))
st.markdown('# ')




st.subheader('Songs - Energy')
Songs=df.head(100)
st.caption('This chart gives us the relationship between the sum of energy to the first 100 songs')
st.plotly_chart(px.histogram(data_frame=Songs,x='song_name',y='energy',hover_name='song_name',height=800,width=1500,template='plotly',color='song_name'))
st.markdown('# ')




st.subheader('Mode - Genre')
Songs=df.head(42304)
st.caption('This histogram give us an idea of the sum of mode genre wise')
Songs=df.sort_values('genre',ascending=False)
st.plotly_chart(px.histogram(data_frame=Songs,x='mode',y='genre',template='seaborn',hover_name='song_name',height=800,width=1100,color='genre'))
st.markdown('# ')




st.subheader('Key - Genre')
dft=df.head(42304)
st.caption('This histogram gives us an idea of the key selection genre wise')
dft=df.sort_values('genre',ascending=False)
st.plotly_chart(px.histogram(data_frame=dft,x='key',y='genre',template='gridon',hover_name='song_name',height=800,width=1100,color='genre'))
st.markdown('# ')




st.subheader('Energy - Genre')
Songs=df.head(42304)
st.caption('This chart shows the bar representation of Energy and genre')
st.plotly_chart(px.bar(data_frame=Songs,x='genre',y='energy',hover_name='song_name',height=800,width=1100,template='none',color='genre'))
st.markdown('# ')




st.subheader('Instrumentalness - Songs - Acousticness')
Songs=df.head(100)
st.caption('This 3D is used to show the relation between Songs,instrumentalness and acousticness')
st.plotly_chart(px.scatter_3d(data_frame=Songs,x='song_name',y='acousticness',z='instrumentalness',hover_name='song_name',height=800,width=1100,template='none',color='song_name'))
st.markdown('# ')




st.subheader('Genre - Danceability')
Songs=df.groupby('genre',as_index=False).count()
st.caption('This pie chart shows the relationship between danceability and genre')
st.plotly_chart(px.pie(data_frame=Songs,names='genre',values='danceability',height=800,width=1100))
st.markdown('# ')




st.subheader('Genre - Loudness')
Songs=df.head(42304)
st.caption('This pie chart shows the sum of loudness to genre')
st.plotly_chart(px.pie(data_frame=Songs,names='genre',values='loudness',template='plotly_dark',height=800,width=1100))
st.markdown('# ')




st.subheader('Songs - Energy - Danceability')
Songs=df.head(100)
st.caption('This chart gives us an idea of the energy and danceability the first 100 songs have')
st.plotly_chart(px.scatter_3d(data_frame=Songs,x='song_name',y='energy',z='danceability',height=800,width=1100,hover_name='song_name',template='plotly_dark',color='danceability'))
st.markdown('# ')




st.subheader('Key - Songs')
Songs=df.head(50)
st.caption('This line chart shows the relation between the first 50 songs and their keys')
st.plotly_chart(px.line(data_frame=Songs,x='key',y='song_name',height=800,width=1100,template='plotly_dark'))
st.markdown('# ')





st.subheader('Genre - Valence')
Songs=df.head(42304)
st.caption('This chart shows the valence genre-wise')
st.plotly_chart(px.pie(data_frame=Songs,names='genre',values='valence',height=800,width=1100))
st.markdown('# ')





st.subheader('Songs - Valence')
Songs=df.head(20)
st.caption('This chart tells us where the valence and key falls (Genre wise)')
st.plotly_chart(px.line(data_frame=Songs,x='song_name',y='valence',height=800,width=1100,template='plotly_dark'))
st.markdown('# ')

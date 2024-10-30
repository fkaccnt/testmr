import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=93e93b4df5d401300c092ec0d4bac84a".format(movie_id))
     data = response.json()
     url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
     return url
def recommend(movie):
     movie_index = movies[movies["title"] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

     recommended_movies = []
     recommended_movies_posters = []
     for i in movies_list:
          movie_id = movies.iloc[i[0]].movie_id
          # Recommended Movies Titles
          recommended_movies.append(movies.iloc[i[0]].title)
          # fetch poster from API
          recommended_movies_posters.append(fetch_poster(movie_id))
     return recommended_movies,recommended_movies_posters

# movies_list = pickle.load(open('movies.pkl','rb'))
# movies_list = movies_list['title'].values
movies_dict = pickle.load(open('movie_dict.pkl',"rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
     'Select From Below or Type',
     movies['title'].values)
#st.write(selected_movie_name)

if st.button('Recommend'):
     #st.write(movies_list)
     names,posters = recommend(selected_movie_name)
     # for i in recommendations:
     #      st.write(i)
     col1, col2, col3, col4, col5 = st.columns(5, gap="small")
     col6, col7, col8, col9, col10 = st.columns(5, gap="small")
     with col1:
          st.text(names[0])
          st.image(posters[0])

     with col2:
          st.text(names[1])
          st.image(posters[1])

     with col3:
          st.text(names[2])
          st.image(posters[2])

     with col4:
          st.text(names[3])
          st.image(posters[3])
     with col5:
          st.text(names[4])
          st.image(posters[4])

     with col6:
          st.text(names[5])
          st.image(posters[5])

     with col7:
          st.text(names[6])
          st.image(posters[6])

     with col8:
          st.text(names[7])
          st.image(posters[7])

     with col9:
          st.text(names[8])
          st.image(posters[8])

     with col10:
          st.text(names[9])
          st.image(posters[9])
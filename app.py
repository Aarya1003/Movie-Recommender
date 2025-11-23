import pickle
import pandas as pd
import streamlit as st

# Set page config
st.set_page_config(
    page_title="Movie Recommender",
    layout="centered",
    initial_sidebar_state="expanded",
    theme="dark"
)


# Recommendation logic
def recommend(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    dist = same[movie_index]
    movies_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    return [movie.iloc[i[0]].title for i in movies_list]

# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)
same = pickle.load(open('same.pkl', 'rb'))

# App UI
st.title('🎬 Movie Recommender System')

option = st.selectbox('Select a movie', movie['title'].values)

if st.button('Recommend'):
    ans = recommend(option)
    st.subheader("Top 5 Recommended Movies:")
    for i in ans:
        st.write(f"👉 {i}")

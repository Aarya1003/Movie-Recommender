import pickle
import pandas as pd
import streamlit as st

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------------
# Custom CSS for better UI
# -----------------------------------
st.markdown("""
    <style>
    body {
        background-color: #0d1b2a;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #0d1b2a, #1b263b);
        color: white;
    }
    .movie-card {
        background-color: #1b263b;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0px;
        border: 1px solid #415a77;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .movie-title {
        font-size: 20px;
        font-weight: bold;
        color: #e0e1dd;
    }
    .subtitle {
        font-size: 26px;
        font-weight: 600;
        color: #e0e1dd;
        text-align: center;
        margin-top: 20px;
    }
    .stButton > button {
        background-color: #e0e1dd;
        color: #1b263b;
        font-size: 18px;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px 20px;
        border: 2px solid #415a77;
    }
    .stButton > button:hover {
        background-color: #ff4d4d;
        color: white;
        border-color: #ff4d4d;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------
# Load Data
# -----------------------------------
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)
same = pickle.load(open('same.pkl', 'rb'))

# -----------------------------------
# Recommendation Logic
# -----------------------------------
def recommend(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    dist = same[movie_index]
    movies_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    return [movie.iloc[i[0]].title for i in movies_list]

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.title("🎬 Movie Recommender")
st.sidebar.markdown("Get movie recommendations using ML & similarity scores.")

# -----------------------------------
# UI Header
# -----------------------------------
st.markdown("<h1 style='text-align:center; color:#e0e1dd;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Discover movies similar to your favourite ones!</p>", unsafe_allow_html=True)

# -----------------------------------
# Main Section
# -----------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    option = st.selectbox("Select a Movie", movie['title'].values)

    recommend_button = st.button("🎯  Recommend", use_container_width=True)

# -----------------------------------
# Show Recommendations
# -----------------------------------
if recommend_button:
    ans = recommend(option)

    st.markdown("<h2 class='subtitle'>🍿 Top 5 Recommended Movies</h2>", unsafe_allow_html=True)

    for i in ans:
        st.markdown(
            f"""
            <div class="movie-card">
                <div class="movie-title">🎥 {i}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

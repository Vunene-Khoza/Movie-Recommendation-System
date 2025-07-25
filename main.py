import streamlit as st
import pickle
import requests

# --- Load Data ---
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# --- Fetch poster from TMDb ---
def fetch_poster(movie_id):
    api_key = "a83c28ab4ae0f30c6f61108116811537"  # 🔐 Replace this with your TMDb API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    return "https://via.placeholder.com/300x450?text=No+Image"

# --- Recommend movies ---
def recommend(title):
    index = movies[movies['title'] == title].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda v: v[1])
    recommended_movies = []
    recommended_posters = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# --- Page Configuration ---
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
        }
        h1 {
            text-align: center;
            color: #FFD700;
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 3rem;
        }
        .stSelectbox>div>div {
            font-size: 18px;
        }
        .movie-card {
            background-color: #ffffff11;
            padding: 10px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1>🎥 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("### Pick a movie you like and get 5 similar recommendations 🍿")

# --- Movie Select ---
selected_movie = st.selectbox("🎬 Select a Movie", movies_list)

# --- Button & Results ---
if st.button("🔍 Show Recommendations"):
    names, posters = recommend(selected_movie)

    st.markdown("### 🎯 You might also like:")
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown(f"""<div class="movie-card">
                <img src="{posters[i]}" style="width:100%; border-radius: 10px;"><br>
                <strong style="color: #FFD700;">{names[i]}</strong>
            </div>""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: white;'>Built with ❤️ using Streamlit & TMDb API</div>", unsafe_allow_html=True)


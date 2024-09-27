import streamlit as st  #  Importing Streamlit which is used to create wep app
import pickle  # Importing pickle,which is used to save and load python objects
import pandas as pd  # Pandas ko import karna, jo data manipulation ke liye yantrana hai
import requests  # Requests ko import karna, jo HTTP requests bhejne ke liye istemal hota hai

# Movie poster fetch karne ke liye function
def fetch_poster(movie_id):
    try:
        # API se movie details lene ke liye request bhejna
        response = requests.get(
            'https://api.themoviedb.org/3/movie/{movie_id}?api_key=a21707c1f45cbc5f5ec474e72afc36cb&language=en-US'.format(
                movie_id=movie_id)
        )
        data = response.json()  # Response ko JSON format mein convert karna
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']  # Poster ka URL return karna
    except Exception as e:
        st.error("Error fetching poster for movie ID {movie_id}: {e}")  # Agar error aaye, toh error message dikhana
        return ""

# Movie ka recommendation dene ke liye function
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]  # Selected movie ka index lena
        distances = similarity[movie_index]  # Similarity matrix se distances lena
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # Top 5 similar movies ko sort karna

        recommended_movies = []  # Recommended movies ka list banana
        recommended_movies_posters = []  # Recommended movies ke posters ka list banana
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id  # Movie ID ko lena
            recommended_movies.append(movies.iloc[i[0]].title)  # Recommended movie ka title add karna
            recommended_movies_posters.append(fetch_poster(movie_id))  # Poster ko fetch karke list mein add karna

        return recommended_movies, recommended_movies_posters  # returns recommended movies and their posters
    except Exception as e:
        st.error(f"Error during recommendation: {e}")  # error message if occurs
        return [], []  # returns empty lists

#  for loading movie dictionary and similarity matrix from pickle files
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # for loading
    movies = pd.DataFrame(movies_dict)  #to convert into dataframe
    similarity = pickle.load(open('similarity.pkl', 'rb'))  # loading similarity matrix
except Exception as e:
    st.error(f"Error loading model files: {e}")  # to show error if occurs

# to show the title of streamlit app
st.header('Movie Recommender System')

# creation of list of movies titles for dropdown
movie_list = movies['title'].values  # to move movie titles in numpy array
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",  # show button for user to select movies
    movie_list
)

# creation of a button to show recommendation
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)  # it will take recommendation of selected movies

    if recommended_movie_names:  # if recommended movie names are available
        # it will create columns to show recommended movies and their posters
        cols = st.columns(5)  # it will create 5 columns
        for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
            with col:  # for every column
                st.text(name)  # to show the name of the movie
                st.image(poster)  # it will show the movie poster
    else:
        st.write("No recommendations available.")  # if there will be no recommendation then it "ll show a message
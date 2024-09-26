# 🎬 Movie Recommender System 🎥

## Overview
This **Movie Recommender System** is designed to provide personalized movie recommendations based on user input. Leveraging machine learning and similarity techniques, this system helps users discover new movies by suggesting films similar to their favorites.

The project makes use of content-based filtering and data from **The Movie Database (TMDb)** API to recommend and display movie posters.

## Features
- 💡 **Content-Based Recommendations**: Suggests movies based on the similarity of the selected movie.
- 🌟 **Movie Posters**: Fetches and displays high-quality movie posters from TMDb API.
- 🎬 **Interactive Interface**: Built with **Streamlit**, offering a clean and user-friendly experience.
- 🔍 **Fast and Accurate Results**: Provides top 5 recommendations within seconds.

## Tech Stack
- **Python** 🐍
- **Pandas**: Data manipulation and handling.
- **Streamlit**: Web interface development.
- **TMDb API**: Fetches movie data and posters.
- **Pickle**: For loading the pre-trained models and movie data.
  
## How It Works
1. The user selects a movie from the provided dropdown.
2. The system computes similarities between movies based on their features (like genres, overview, etc.).
3. It returns the top 5 most similar movies along with their posters.
4. The recommendations are displayed in a grid layout for easy viewing.

## Project Structure
```
Movie-Recommender-System/
│
├── model/                   
│   ├── movie_dict.pkl        # Pickled movie data
│   └── similarity.pkl        # Pickled similarity matrix
│
├── app.py                    # Main Streamlit app script
│
└── README.md                 # Project documentation
```

## API Integration
We use the **TMDb API** to fetch movie information, including movie posters. Ensure to replace the API key with your own if you're deploying the project independently.

## Future Enhancements
- 🎯 Add **collaborative filtering** for better personalized recommendations.
- 🌍 Implement multi-language support.
- 📱 Improve UI for mobile devices.
- 🧠 Integrate more sophisticated machine learning models.

## Screenshots
![Screenshot 2024-09-26 220951](https://github.com/user-attachments/assets/06fdb0ba-f16c-499b-a67e-d86e8dde84f9)
![Screenshot 2024-09-26 221016](https://github.com/user-attachments/assets/af13cf23-f038-41eb-b785-d8ba8e6fecfa)
![Screenshot 2024-09-26 222342](https://github.com/user-attachments/assets/40f88d2e-3250-49d2-a6fb-313f02026c25)

## Contact
Feel free to reach out via [LinkedIn](www.linkedin.com/in/harsh-dwivedi-7a7539212) for any queries or collaborations.

# 🎬 Movie-Recommendation-System

A sophisticated **content-based movie recommendation system** built with **machine learning** and deployed as an interactive web application using **Streamlit**.

---

## 🌟 Features

- **Content-Based Filtering**: Recommends movies based on plot, genre, and movie characteristics  
- **Interactive Web Interface**: Beautiful, responsive Streamlit web application  
- **Movie Posters**: Integration with **TMDb API** for high-quality movie posters  
- **Smart Search**: Fuzzy matching for movie titles  
- **Similarity Scoring**: Shows how closely matched each recommendation is  
- **Responsive Design**: Works great on desktop and mobile devices  

---

## 🛠️ Technology Stack

- **Python 3.8+**  
- **Machine Learning**: `scikit-learn`, `pandas`, `numpy`  
- **Web Framework**: `Streamlit`  
- **API Integration**: **TMDb (The Movie Database) API**  
- **Data Processing**: **TF-IDF Vectorization**, **Cosine Similarity**

---

## 📋 Prerequisites

Before running this project, make sure you have:

- **Python 3.8 or higher** installed  
- A **TMDb API key** (free registration at [themoviedb.org](https://www.themoviedb.org/))  

---

### 📁 Download/Prepare Data Files

Make sure you have these files in your project directory:

- `movies_list.pkl` - Preprocessed movie dataset  
- `similarity.pkl` - Precomputed similarity matrix  

---

## ▶️ Run the Application

```bash
streamlit run app.py
```
The app will open in your browser at:
http://localhost:8501


# 🧠 How It Works
1. Data Preprocessing

Combines movie overview, genre, and title into "tags"
Cleans and preprocesses text data
Handles missing values

2. Feature Extraction

Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
Converts text into numerical vectors
Creates a feature matrix of 10,000+ movies

3. Similarity Calculation

Computes cosine similarity between all movie pairs
Creates a 10,000 x 10,000 similarity matrix
Enables fast recommendation lookup

4. Recommendation Generation

Finds the input movie in the dataset
Retrieves similarity scores for all other movies
Returns top N most similar movies

📊 Dataset
The model is trained on The Movie Database (TMDb) dataset containing:

10,000+ movies
Movie titles, overviews, genres
Release dates, ratings, and popularity scores
Unique movie IDs for API integration

Data Sources

TMDb 5000 Movie Dataset
The Movie Database API
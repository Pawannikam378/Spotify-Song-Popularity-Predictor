import pandas as pd

def preprocess():
    df = pd.read_csv("E:\D Drive Data\Project\Spotify Song Prediction System\Spotify-Song-Popularity-Predictor\data\spotify_data.csv")

    df = df.dropna()
    df = df.drop_duplicates()
    df['energy_dance'] = df['energy'] * df['danceability']
    df['tempo_bucket'] = pd.cut(df['tempo'], bins=[0, 90, 120, 200], labels=[0,1,2])
    features = [
        'danceability',
        'energy',
        'loudness',
        'speechiness',
        'acousticness',
        'instrumentalness',
        'liveness',
        'valence',
        'tempo'
    ]

    X = df[features]
    y = df['popularity']

    return X, y
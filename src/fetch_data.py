import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

CLIENT_ID = "aea1a425b3d64a90b404f07fb06a143b"
CLIENT_SECRET = "153c1d3df441488b803a321969e44b1d"

auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(
    auth_manager=auth_manager,
    requests_timeout=10,
    retries=3
)

queries = [
    "bollywood", "arijit singh"
]

def fetch_data():
    all_data = []

    for query in queries:
        print(f"Fetching: {query}")
        try: 
            results = sp.search(q=query, type='track', limit=1, market="IN")
            tracks = results['tracks']['items']
            track_ids = [track['id'] for track in tracks]
            features_list = sp.audio_features(track_ids)
            
            for i, track in enumerate(tracks):
                features = features_list[i]

                if features is None:
                    continue

                features['popularity'] = track['popularity']
                features['track_name'] = track['name']
                features['artist'] = track['artists'][0]['name']

                all_data.append(features)

            time.sleep(0.5)

        except Exception as e:
            print("Error:", e)

    df = pd.DataFrame(all_data)
    df.to_csv("data/spotify_data.csv", index=False)
    print("Done!")

if __name__ == "__main__":
    fetch_data()
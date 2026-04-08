import spotify
from spotify.oauth2 import SpotifyClientCredentials
import pandas as pd

CLIENT_ID = "ID"
CLIENT_SECRET = ""

def fetch_tracks(query="year:2023", limit=50):
    auth = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotify.Spotify(auth_manager=auth)

    result = sp.search(q=query, type='track', limit=limit)
    tracks = result['tracks']['items']

    track_ids = [track['id'] for track in tracks]
    features = sp.audio_features(track_ids)

    df = pd.DataFrame(features)
    return df


if __name__ == "__main__":
    df = fetch_tracks()
    df.to_csv("spotify_tracks.csv", index=False)
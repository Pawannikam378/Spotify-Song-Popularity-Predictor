import pandas as pd 

def preprocess():
    df - pd.read_csv("data/raw.csv")
    df = df.dropna()
    df = df.drop_duplicates()

    X = df.drop(columns=['popularity'])
    y = df['popularity']

    return X, y

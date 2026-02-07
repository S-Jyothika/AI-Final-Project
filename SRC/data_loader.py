import pandas as pd

def load_data():
    df = pd.read_csv('data/NetflixSimple.csv')
    df = df.fillna('')
    return df

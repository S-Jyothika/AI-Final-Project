import pandas as pd

def load_data():
    df = pd.read_csv('/content/drive/MyDrive/AI Final Project/NetflixSimple.csv')
    df = df.fillna('')
    return df

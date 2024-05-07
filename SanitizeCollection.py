import pandas as pd

def sanitize_collection():
    collection_df = pd.read_csv('Collections/patrick.csv', header=0)
    owned_df = collection_df[(collection_df['Normal count'] != 0) | (collection_df['Golden count'] != 0)].copy()
    return owned_df

sanitize_collection()
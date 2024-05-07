import pandas as pd
import json

def sanitize_collection():
    collection_df = pd.read_csv('Collections/patrick.csv', header=0)
    owned_df = collection_df[(collection_df['Normal count'] != 0) | (collection_df['Golden count'] != 0)].copy()
    return owned_df


def get_all_cards():
    with open('cards.collectible.json', 'r', encoding="utf8") as file:
        all_cards_data = json.load(file)
        # print(all_cards_data[0])
    return all_cards_data

def update_collection(all_cards_data, owned_df):
    
    owned_df.set_index('Id', inplace=True)
    
    for item in all_cards_data:
        if item['dbfId'] in owned_df.index:
            owned_df.loc[item['dbfId'],'rarity'] = item['rarity']
            owned_df.loc[item['dbfId'], 'cardClass'] = item['cardClass']
            try:
                owned_df.loc[item['dbfId'], 'set'] = item['set']
            except:
                continue
            owned_df.loc[item['dbfId'], 'type'] = item['type']
            
    owned_df.reset_index(inplace=True)
    
    return owned_df


owned_df = sanitize_collection()
all_cards_data = get_all_cards()
updated_df = update_collection(all_cards_data, owned_df)
print(updated_df)

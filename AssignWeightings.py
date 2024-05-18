import pandas as pd


def assign_weights(class_specific_standard_df):
    
    rarity_weights_dict = {
        'COMMON': 0.50,            
        'RARE': 0.30,              
        'EPIC': 0.17,              
        'LEGENDARY': 0.02          
    }
    
    class_weights_dict = {
        'NEUTRAL': 0.1,              
        'DRUID': 0.9,
        'WARRIOR': 0.9,
        'SHAMAN': 0.9,
        'PRIEST': 0.9,
        'MAGE': 0.9,
        'DEMONHUNTER': 0.9,
        'DEATHKNIGHT': 0.9,
        'ROGUE': 0.9,
        'PALADIN': 0.9,
        'HUNTER': 0.9,
        'WARLOCK': 0.9   
    }
    
    class_specific_standard_df['rarity_weight'] = class_specific_standard_df['rarity'].map(rarity_weights_dict)
    class_specific_standard_df['class_weight'] = class_specific_standard_df['cardClass'].map(class_weights_dict)
    
    class_specific_standard_df['rarity_weight'] = pd.to_numeric(class_specific_standard_df['rarity_weight'])
    class_specific_standard_df['class_weight'] = pd.to_numeric(class_specific_standard_df['class_weight'])

    class_specific_standard_df['combined'] = (class_specific_standard_df['rarity_weight'] + class_specific_standard_df['class_weight'])
    class_specific_standard_df['weights'] = (class_specific_standard_df['combined'] / class_specific_standard_df['combined'].sum())
    return class_specific_standard_df
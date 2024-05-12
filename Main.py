import random
import tkinter as tk
from SanitizeCollection import sanitize_collection, update_collection, get_all_cards
from GetStandardSets import getAccessToken, get_standard_sets, get_standard_set_ids
from Collection import build_standard_cardset
from CardImage import getCardImages
from GUItest import create

### Access Token
access_token = getAccessToken()

### Get All owned cards from collection
owned_cards_df = sanitize_collection()

### Update owned cards for more paramaters
all_cards = get_all_cards()
updated_owned_df = update_collection(all_cards, owned_cards_df)

### Get Standard Sets
standard_sets = get_standard_sets(access_token)
standard_set_ids = get_standard_set_ids(standard_sets, access_token)
standard_cards_id_list = build_standard_cardset(access_token)

### Random Class Selection
possible_classes = ['MAGE', 'PRIEST', 'PALADIN', 'DRUID', 'DEMONHUNTER', 'ROGUE', 'WARRIOR', 'WARLOCK', 'HUNTER', 'SHAMAN', 'DEATHKNIGHT']
random_selection_classes = random.sample(possible_classes, 3)
print(random_selection_classes)

while True:
    selected_class = input("Please choose a class. \n").upper()
    
    if selected_class.upper() in random_selection_classes:
        print(f"You Chose {selected_class}")
        break
    else:
        print("Invalid input. Please choose an available class.")
        print(f"{selected_class} not in {random_selection_classes}")

### Organize Cards from collection by standard + class
class_specific_df = updated_owned_df[(updated_owned_df['cardClass'] == selected_class.upper()) | (updated_owned_df['cardClass'] == 'NEUTRAL')].copy()
class_specific_standard_df = class_specific_df[(class_specific_df['Id'].isin(standard_cards_id_list))].copy()
# print(class_specific_standard_df)

### Build Deck
deck_card_ids = []
deck_card_names = []
# random_card_ids = []


while len(deck_card_names) < 30:
    random_card_ids = []
    random_cards_selected = class_specific_standard_df.sample(3)
    random_cards_names = random_cards_selected['Name'].tolist()
    print(random_cards_names)
    for card in random_cards_names:
        card_dict = next(item for item in all_cards if item["name"] == card)
        random_card_ids.append(card_dict["id"])

    images = getCardImages(random_card_ids)
    create(images)
    
    while True:
        card = input("Please choose a card. \n")
        
        if card in random_cards_names:
            print(f"You Chose {card}")
            deck_card_names.append(card)
            break
        else:
            print("Invalid input. Please choose an available class.")
            print(f"{card} not in {random_cards_names}")

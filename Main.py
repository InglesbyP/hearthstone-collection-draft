import random
from SanitizeCollection import sanitize_collection, update_collection, get_all_cards
from GetStandardSets import getAccessToken, get_standard_sets, get_standard_set_ids

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

### Organize Cards from collection by standard + class


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

### Build Deck
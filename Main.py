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


### Build Deck
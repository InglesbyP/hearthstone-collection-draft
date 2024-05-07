from SanitizeCollection import sanitize_collection
from GetStandardSets import getAccessToken, get_standard_sets, get_standard_set_ids

### Access Token
access_token = getAccessToken()

### Get All owned cards from collection
owned_cards_df = sanitize_collection()

### Get Standard Sets
standard_sets = get_standard_sets(access_token)
standard_set_ids = get_standard_set_ids(standard_sets, access_token)

### Organize Cards from collection by standard + class


### Random Class Selection


### Build Deck
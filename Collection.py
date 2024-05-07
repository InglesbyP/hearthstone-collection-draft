import requests
from GetStandardSets import get_standard_sets, get_standard_set_ids, getAccessToken


access_token = getAccessToken()
standard_sets = get_standard_sets(access_token)
standard_set_ids = get_standard_set_ids(standard_sets, access_token)

print(standard_set_ids)

############
# Make Card Request
############

# Define the API endpoint URL
# Get specific card ID
api_url = 'https://us.api.blizzard.com/hearthstone/cards/111320?locale=en_US'

# Set up headers with the Authorization Bearer token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Set up query parameters for the API endpoint
params = {
    'namespace': 'dynamic-us'
}

# Make the GET request to the API endpoint
response = requests.get(api_url, headers=headers, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and display the response data
    token_data = response.json()
    # arr_data = json.loads(token_data)
    print("Token Data For Card:")
    print(token_data)
else:
    print(f"Failed to retrieve token data. Status code: {response.status_code}")
    print(f"Response content: {response.text}")
    
print("#####################")
# print(arr_data)
# print(token_data["id"])

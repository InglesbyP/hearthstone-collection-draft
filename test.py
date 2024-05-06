import requests

############
# Init
############

# Define client credentials
client_id = '39e4720a9948476a9cb03b865c47b1ad'
client_secret = 'AKeFRTAH7HDtnSBKvIJ7nkLwfOC6rKHg'

############
# Get Auth token
############

# Define the token URL
token_url = 'https://us.battle.net/oauth/token'  # Update the URL according to the region

# Set up the payload data
data = {
    'grant_type': 'client_credentials'
}

# Set up basic authentication using client_id and client_secret
auth = (client_id, client_secret)

# Make the POST request to obtain the access token
response = requests.post(token_url, data=data, auth=auth)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response to get the access token
    token_data = response.json()
    access_token = token_data.get('access_token')
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to obtain access token. Status code: {response.status_code}")
    print(f"Response content: {response.text}")

############
# Make Request
############

# Define the API endpoint URL
# Get specific card ID
api_url = 'https://us.api.blizzard.com/hearthstone/cards/678?locale=en_US'

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
    print("Token Data:")
    print(token_data)
else:
    print(f"Failed to retrieve token data. Status code: {response.status_code}")
    print(f"Response content: {response.text}")


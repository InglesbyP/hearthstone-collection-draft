import requests
import pandas as pd
from GetStandardSets import get_standard_sets, get_standard_set_ids, getAccessToken


# access_token = getAccessToken()
# standard_sets = get_standard_sets(access_token)
# standard_set_ids = get_standard_set_ids(standard_sets, access_token)


def build_standard_cardset(access_token):
    ############
    # Make Card Request
    ############

    # Define the API endpoint URL
    # Get specific card ID
    api_url = 'https://us.api.blizzard.com/hearthstone/cards'

    # Set up headers with the Authorization Bearer token
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Set up query parameters for the API endpoint
    params = {
        'locale': 'en-us',
        'set': 'standard',
        'pageSize': '500',
        'page': '1'
    }

    # Make the GET request to the API endpoint
    response = requests.get(api_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and display the response data
        token_data = response.json()
        df = pd.DataFrame.from_dict(token_data)
        df = pd.DataFrame(df.cards.to_list(), index = df.index)
        
    else:
        print(f"Failed to retrieve token data. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
    
    
    ## request 2
    params = {
        'locale': 'en-us',
        'set': 'standard',
        'pageSize': '500',
        'page': '2'
    }
    
    # Make the GET request to the API endpoint
    response = requests.get(api_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and display the response data
        token_data = response.json()
        df2 = pd.DataFrame.from_dict(token_data)
        df2 = pd.DataFrame(df2.cards.to_list(), index = df2.index)
        
    else:
        print(f"Failed to retrieve token data. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
        
    
    ## request 2
    params = {
        'locale': 'en-us',
        'set': 'standard',
        'pageSize': '500',
        'page': '3'
    }
    
    # Make the GET request to the API endpoint
    response = requests.get(api_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and display the response data
        token_data = response.json()
        df3 = pd.DataFrame.from_dict(token_data)
        df3 = pd.DataFrame(df3.cards.to_list(), index = df3.index)
        
    else:
        print(f"Failed to retrieve token data. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
    
    concat1_df = df._append(df2)
    concat2_df = concat1_df._append(df3)
    standard_id_list = concat2_df['id'].tolist()
    # print(standard_id_list)
    return standard_id_list
    
# build_standard_cardset(access_token)
    
    


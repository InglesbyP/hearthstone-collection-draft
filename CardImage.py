import requests
from GetStandardSets import getAccessToken
from PIL import Image
from io import BytesIO

access_token = getAccessToken()

def getCardImages(card_IDs):
    
    images = []
    
    api_url = 'https://art.hearthstonejson.com/v1/render/latest/enUS/256x/'+ card_IDs[0] +'.png'
    api_url2 = 'https://art.hearthstonejson.com/v1/render/latest/enUS/256x/'+ card_IDs[1] +'.png'
    api_url3 = 'https://art.hearthstonejson.com/v1/render/latest/enUS/256x/'+ card_IDs[2] +'.png'
    
    response = requests.get(api_url)
    
    image_1 = Image.open(BytesIO(response.content))
    images.append(image_1)
    
    response2 = requests.get(api_url2)
    
    image_2 = Image.open(BytesIO(response2.content))
    images.append(image_2)
    
    response3 = requests.get(api_url3)
    
    image_3 = Image.open(BytesIO(response3.content))
    images.append(image_3)
    
    return images
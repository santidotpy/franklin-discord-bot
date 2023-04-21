import requests

def meme():
    r = requests.get('https://meme-api.com/gimme')
    response = r.json()
    meme_img = response['url']
    return meme_img
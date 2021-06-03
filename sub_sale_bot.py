import requests
import os
import tweepy
from dotenv import load_dotenv
from datetime import datetime

HT_API = 'https://www.harristeeter.com/api/v1/ffo/stores/330/departments/55faa06f72e49e4958f6865c/categories/5608cffe87a5f77c3ff67592/products?Private=false'
COOKIES = 'cookieConsentInteraction=true; targetingCookies=allow; _gag=akdmMVFvbFhZSzRoc25ZV0ZkTkhPL2RUbzdFdTEvei9pcHRzcUJEZzdnMkxsRWg4NUkyb2JRTC9BSTJOU0QwRXBFdHZRbzZFVXBxdk5ZWURMSGtwR1laa0JURG0wbm1hNzdaYjE1YWtmL3FJWjlnZWxBTHpGTGJBQW1HWkhXdDhNd2lmNnh5ZjRuMWRjMXRQRWdRN3pxWFdJaDhIQjBiZE1JTXY4ckl2T2hqUk04Rm5UdXZCcGM5YldHa1pnSm9xbk0vRGdzSktQYlBIbXJLM0N3SUxKQlpnNTRXWVNHQT0=; _i=bVEvZlFhSkplTWhsNnlSNmI1WUxkL2RRMjhSVnZaRDl6K1EzOGtxZy9nQ1VqeDRvZzh2NkwwVzRTbzJYVnpzVnRTUS9GZG5kSGRtOFR3PT0=; _j=aXgySkdmMWFhOUY2K3o5aWNKNEFQNmNCd05kSHJZSGwwdmNzN2xHZy9nQ1VqeDRvZzh2NkwwVzRTbzJYVnpzVnRTUS9GZG5kSGRtOFR3PT0=; _k=bVEvZlFhSkplTWhsNnlSNmI1WUxkK1ZDalp3S3JvUGswUFFzNmxXbzlVakUzZ1U3a2R2ck4xaXJVWkdNVnpzVnRTUS9GZG5kSGRtOFR3PT0=; HTAPIADMSESID=s:6LMbL42LmqyGQncc15ILCSU1sGkinc4j.lgTkFLBj2ZRbC/pE08G1wMtEy0dlRI+eH7krVEv0Uac'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
REFERER = 'https://www.harristeeter.com/orderahead/selectstore/store/330/departmentsGroup/55fa9932ec2c944f582c2785/departments/55faa06f72e49e4958f6865c/categories/5608cffe87a5f77c3ff67592/products?activeTab=items'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
NORMAL_PRICE = 6.99

headers = {
    'cookie': COOKIES,
    'user-agent': USER_AGENT,
    'referer': REFERER
}
response = requests.get(HT_API, headers=headers).json()
special_price = response['Data'][0]['SpecialPrice']

if special_price and float(special_price) < NORMAL_PRICE:
    special_price = float(special_price)
    
    load_dotenv(os.path.join(BASEDIR, '.env'))
    auth = tweepy.OAuthHandler(os.environ['API'], os.environ['APISecret'])
    auth.set_access_token(os.environ['AccessToken'], os.environ['AccessTokenSecret'])
    api = tweepy.API(auth)
    
    # Include the date to avoid a duplicate tweet
    date = str(datetime.today().strftime('%x'))
    api.update_status(date + '\nHarris Teeter subs are on sale for $' + str(special_price))
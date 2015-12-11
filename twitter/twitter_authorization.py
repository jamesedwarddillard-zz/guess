from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

from twitter_secret import CLIENT_KEY, CLIENT_SECRET
from twitter_urls import *


def get_access_token():
    client = BackendApplicationClient(client_id = CLIENT_KEY)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(
        token_url=REQUEST_TOKEN_URL,
        client_id=CLIENT_KEY,
        client_secret=CLIENT_SECRET
    )
    return token['access_token']

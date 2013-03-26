import urllib.request
import urllib.parse
import time
import pprint
import uuid 
import oauthlib.oauth1 as oauth

class Authenticate:
  def connect(self):
    # Our settings are stored in a text file outside of the app root
    settings = open("../twirp_settings.txt",'r')
    consumer_key = settings.readline().rstrip()
    consumer_secret = settings.readline().rstrip()
    client = oauth.Client(consumer_key,
      client_secret = consumer_secret)
    uri, headers, body = client.sign('https://api.twitter.com/oauth/request_token')

    token_request = urllib.request.Request("https://api.twitter.com/oauth/request_token")
    token_request.headers = headers
    token_response = urllib.request.urlopen(token_request)

    # Parse into something usable
    decoded_response = token_response.read().decode()
    split_response = decoded_response.split("&")
    response_dictionary = {}

    # Parse into dictionary
    for chunk in split_response: 
      chunk = chunk.split("=")
      response_dictionary[chunk[0]] = chunk[1]
    
    if(response_dictionary['oauth_callback_confirmed']): 
      print('Callback confirmed')
    print('Please Visit: https://api.twitter.com/oauth/authenticate?oauth_token=' + response_dictionary['oauth_token'] + ' to authorize this app.')
    pin = input("Please enter the provided pin: ")



    client = oauth.Client(consumer_key,
      client_secret = consumer_secret)
    uri, headers, body = client.sign('https://api.twitter.com/oauth/access_token?oauth_verifier=' + pin)
    access_token_request = urllib.request.Request("https://twitter.com/oauth/access_token?oauth_verifier=" + pin)
    access_token_request.headers = headers
    access_token_response = urllib.request.urlopen(access_token_request)

userconnect = Authenticate()
userconnect.connect()

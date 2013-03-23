import urllib.request
import urllib.parse
import time

class Authenticate:
  def connect(self):
    # Our settings are stored in a text file outside of the app root
    settings = open("../twirp_settings.txt",'r')
    consumer_key = settings.readline()
    consumer_secret = settings.readline()

    build_oauth_header(consumer_key,consumer_secret)
    # TODO: Have to attach above oauth header to make this request not return 403

    token_request = urllib.request.Request("https://api.twitter.com/oauth/request_token")
    token_response =  urllib.request.urlopen(token_request)
    page = token_response.read()
    print(page)
    #print url to get my pin
    #pin = input('Enter the pin provided by twitter: ')


def build_oauth_header(consumer_key,consumer_secret):
  oauth_consumer_key=consumer_key
  oauth_nonce=consumer_secret 
  oauth_signature='' 
  oauth_signature_method="HMAC-SHA1", 
  oauth_timestamp= time.time()
  oauth_token='' 
  oauth_version="1.0"

userconnect = Authenticate()
userconnect.connect()

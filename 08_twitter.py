from tweepy import OAuthHandler, Stream

from secret import consumer_key, access_token, consumer_secret, access_token_secret

def mi_observable(o, s):
    pass

listener = TweetListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listener)
keywords = ['estado de alarma']
stream.filter(track=keywords)
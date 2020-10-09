# Autenticación con Twitter y seguimiento con Twitter Streaming API
from rx import create
from tweepy import OAuthHandler, Stream, StreamListener

from printer import Printer
from secret import consumer_key, access_token, consumer_secret, access_token_secret


def mi_observable(keywords):
    def observe_tweets(o, s):
        class TweetListener(StreamListener):
            def on_data(self, data):
                o.on_next(data)

            def on_error(self, status):
                o.on_error(status)

        listener = TweetListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)
        stream.filter(track=keywords)

    return create(observe_tweets)


keywords = ['estado de alarma']

mi_observable(keywords).pipe(

).subscribe(Printer())
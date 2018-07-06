from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import config as credentials  # fill the file with your own credentials


def authentication():
    auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
    return auth


class StdOutListener(StreamListener):
    def on_data(self, tweet_info):
        try:
            print(tweet_info)
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True


    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    keywords_list = ["WorldCup"]
    languages_list = ["en"]

    auth = authentication()
    listener = StdOutListener()
    # stream tweets
    stream = Stream(auth, listener)

    # filter Twitter stream
    stream.filter(languages=languages_list, track=keywords_list)

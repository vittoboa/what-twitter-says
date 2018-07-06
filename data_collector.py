from json import loads
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import config as credentials  # fill the file with your own credentials


def authentication():
    auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
    return auth


def get_text(text_info):
    if text_info["truncated"]:
        # if the original text has been truncated get the full text
        text = text_info["extended_tweet"]["full_text"]
    else:
        text = text_info["text"]
    return text


class StdOutListener(StreamListener):
    def on_data(self, tweet_info):
        try:
            ## clean tweet informations ##
            # convert the tweet_info from string to dictionary
            tweet_info = loads(tweet_info)
            # get the time of the tweet
            tweet_time = tweet_info["created_at"].split()[3]
            # get the text of the tweet
            if "retweeted_status" in tweet_info.keys():
                # if it's a retweet get the original tweet text
                tweet_text = get_text(tweet_info["retweeted_status"])
            else:
                tweet_text = get_text(tweet_info)
            # make the tweet one single line
            tweet_text = tweet_text.replace("\n", " ")
            # format the tweet
            tweet = "{0}\n{1}\n".format(tweet_time, tweet_text)

            print(tweet)

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

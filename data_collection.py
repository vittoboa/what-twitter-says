import json
import tweepy
import csv

import config as credentials  # fill the file with your own credentials
import constants as K

def authentication():
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
    return auth


def get_text(text_info):
    is_truncated = text_info["truncated"]
    return text_info["extended_tweet"]["full_text"] if is_truncated else text_info["text"]


def create_file():
    with open(K.FETCHED_TWEETS_FILE, 'a', newline='') as tweets_f:
        writer = csv.DictWriter(tweets_f, fieldnames=K.FIELDNAMES)
        # write the column titles in the first row
        writer.writeheader()


class StdOutListener(tweepy.StreamListener):
    def on_data(self, tweet_info):
        ## clean and store the tweets ##
        try:
            ## clean tweet informations ##
            # convert the tweet_info from string to dictionary
            tweet_info = json.loads(tweet_info)
            # get the time of the tweet
            tweet_time = tweet_info["created_at"].split()[3]
            # get the text of the tweet
            is_retweet = "retweeted_status" in tweet_info.keys()
            text_info  = tweet_info["retweeted_status"] if is_retweet else tweet_info
            tweet_text = get_text(text_info)

            ## store the tweet ##
            with open(K.FETCHED_TWEETS_FILE, 'a', newline='') as tweets_f:
                writer = csv.DictWriter(tweets_f, fieldnames=K.FIELDNAMES)
                writer.writerow({K.FIELDNAMES[0]: tweet_time, K.FIELDNAMES[1]: tweet_text})

        except BaseException as e:
            print(f"Error on_data {e}")

        return True


    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    create_file()

    auth = authentication()
    listener = StdOutListener()
    # stream tweets
    stream = tweepy.Stream(auth, listener)

    # filter Twitter stream
    stream.filter(languages=K.LANGUAGES_LIST, track=K.KEYWORDS_LIST)

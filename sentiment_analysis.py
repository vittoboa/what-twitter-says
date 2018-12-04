from textblob import TextBlob
import csv

import constants as K


def is_sentiment_meaningful(sentiment_score):
    return abs(sentiment_score) > 0.15


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    return sentiment if is_sentiment_meaningful(sentiment) else 0    


if __name__ == '__main__':
    sentiment_per_minute = {}

    with open(K.CLEANED_TWEETS_FILE, 'r') as f_input:
        reader = csv.reader(f_input)
        for time, text in reader:
            sentiment_per_minute[time] = sentiment_per_minute.get(time, 0) + get_sentiment(text)

    with open(K.SENTIMENT_TWEETS_FILE, 'w') as f_output:
        writer = csv.writer(f_output)
        writer.writerows(row for row in sentiment_per_minute.items())

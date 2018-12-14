from textblob import TextBlob
import csv
import collections

import constants as K


def is_sentiment_meaningful(sentiment_score):
    return abs(sentiment_score) > 0.15


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    return sentiment if is_sentiment_meaningful(sentiment) else 0    


if __name__ == '__main__':
    sentiment_overtime, words_count = collections.Counter(), collections.Counter()

    with open(K.CLEANED_TWEETS_FILE, 'r') as f_input:
        reader = csv.reader(f_input)
        for time, text in reader:
            sentiment_overtime[time] += get_sentiment(text)
            words_count.update(text.split())

    with open(K.SENTIMENT_TWEETS_FILE, 'w') as f_output_sentiment:
        writer_sentient = csv.writer(f_output_sentiment)
        writer_sentient.writerows(row for row in sentiment_overtime.items())

    with open(K.WORDS_COUNT_FILE, 'w') as f_output_words_count:
        writer_words_count = csv.writer(f_output_words_count)
        writer_words_count.writerows(row for row in words_count.most_common())

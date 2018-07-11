import csv
import re

import constants as K


def remove_multiple_whitespaces(text):
    return " ".join(text.split())


def remove_urls(text):
    return re.sub(r'http\S+', '', text)


if __name__ == '__main__':
    with open(K.FETCHED_TWEETS_FILE, newline='') as tweets_f:
        reader = csv.DictReader(tweets_f)
        for row in reader:
            text = row[K.FIELDNAMES[1]]
            text_cleaned = remove_multiple_whitespaces(text)
            text_cleaned = remove_urls(text_cleaned)

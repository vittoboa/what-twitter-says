import csv

import constants as K


def remove_multiple_whitespaces(text):
    return " ".join(text.split())


if __name__ == '__main__':
    with open(K.FETCHED_TWEETS_FILE, newline='') as tweets_f:
        reader = csv.DictReader(tweets_f)
        for row in reader:
            text = row[K.FIELDNAMES[1]]
            text_cleaned = remove_multiple_whitespaces(text)

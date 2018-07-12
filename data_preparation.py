import csv
import re

import constants as K


def remove_non_alphanumeric(text):
    return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


if __name__ == '__main__':
    with open(K.FETCHED_TWEETS_FILE, newline='') as tweets_f:
        reader = csv.DictReader(tweets_f)
        for row in reader:
            text = row[K.FIELDNAMES[1]]
            text = remove_non_alphanumeric(text)
            print(text)
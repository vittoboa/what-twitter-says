import csv
import re
from nltk.corpus import stopwords

import constants as K


def remove_seconds(time):
    hour, minute, _ = time.split(":")
    return "{}:{}".format(hour, minute)


def remove_non_alphanumeric(text):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


def remove_stopwords(text):
    return " ".join(word for word in text.split() if word not in stopwords)


def replace_slang(text):
    return " ".join(K.SLANG.get(word, word) for word in text.split())


def clean_text(text):
    text = remove_non_alphanumeric(text)
    text = text.lower()
    text = replace_slang(text)
    text = remove_stopwords(text)

    return text


def clean_time(time):
    time = remove_seconds(time)

    return time


if __name__ == '__main__':
    stopwords = stopwords.words("english")

    with open(K.FETCHED_TWEETS_FILE, 'r') as f_input, open(K.CLEANED_TWEETS_FILE, 'w') as f_output:
        reader = csv.reader(f_input)
        writer = csv.writer(f_output)

        reader_sorted_by_time = sorted(reader, key=lambda row:row[0])
        for time, text in reader_sorted_by_time:
            time = clean_time(time)
            text = clean_text(text)
            writer.writerow((time, text))

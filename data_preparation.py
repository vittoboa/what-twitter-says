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


if __name__ == '__main__':
    stopwords = stopwords.words("english")

    with open(K.FETCHED_TWEETS_FILE, 'r') as f_input, open(K.CLEANED_TWEETS_FILE, 'w') as f_output:
        reader = csv.reader(f_input)
        writer = csv.writer(f_output)
        
        reader_sorted_by_time = sorted(reader, key=lambda row:row[0])
        for row in reader_sorted_by_time:
            # get raw time and text
            time, text = row

            # clean time
            time = remove_seconds(time)

            # clean text
            text = remove_non_alphanumeric(text)
            text = text.lower()
            text = remove_stopwords(text)

            # store time and text in the file
            writer.writerow((time, text))

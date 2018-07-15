import csv
import re

import constants as K


def remove_seconds(time):
    # get only hour and minute
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    return "{}:{}".format(hour, minute)


def remove_non_alphanumeric(text):
    return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


def remove_match_hashtags(text):
    return " ".join(word for word in text.split()
        if not (K.TEAM_HOME_ABBREVIATION in word 
            and K.TEAM_AWAY_ABBREVIATION in word))


if __name__ == '__main__':
    with open(K.FETCHED_TWEETS_FILE, 'r', newline='') as f_input, open(K.CLEANED_TWEETS_FILE, 'w') as f_output:
        reader = csv.DictReader(f_input)
        writer = csv.DictWriter(f_output, fieldnames=K.FIELDNAMES)

        # write the column names in the first row
        writer.writeheader()
        
        reader_sorted_by_time = sorted(reader, key=lambda row:row[K.FIELDNAMES[0]])
        for row in reader_sorted_by_time:
            # get raw time and text
            time, text = row[K.FIELDNAMES[0]], row[K.FIELDNAMES[1]]

            # clean time
            time = remove_seconds(time)

            # clean text
            text = remove_non_alphanumeric(text)
            text = text.lower()
            text = remove_match_hashtags(text)

            # store time and text in the file
            writer.writerow({
                K.FIELDNAMES[0]: time,
                K.FIELDNAMES[1]: text
            })

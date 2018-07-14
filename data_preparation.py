import csv
import re

import constants as K


def remove_non_alphanumeric(text):
    return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


if __name__ == '__main__':
    with open(K.FETCHED_TWEETS_FILE, 'r', newline='') as f_input, open(K.CLEANED_TWEETS_FILE, 'w') as f_output:
        reader = csv.DictReader(f_input)
        writer = csv.DictWriter(f_output, fieldnames=K.FIELDNAMES)

        # write the column names in the first row
        writer.writeheader()
        
        for row in reader:
            # get raw time and text
            time, text = row[K.FIELDNAMES[0]], row[K.FIELDNAMES[1]]
            
            # clean text
            text = remove_non_alphanumeric(text)
            text = text.lower()

            # store time and text in the file
            writer.writerow({
                K.FIELDNAMES[0]: time,
                K.FIELDNAMES[1]: text
            })

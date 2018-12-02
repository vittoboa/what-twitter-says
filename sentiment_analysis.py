from textblob import TextBlob
import csv

import constants as K


def file_lines_count(file):
    return sum(1 for row in file)


def is_last_row(row_count, current_row):
    return current_row == row_count


def is_sentiment_meaningful(sentiment_score):
    return abs(sentiment_score) > 0.15


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    return sentiment if is_sentiment_meaningful(sentiment) else 0    


if __name__ == '__main__':
    with open(K.CLEANED_TWEETS_FILE, 'r', newline='') as f_input, open(K.SENTIMENT_TWEETS_FILE, 'w') as f_output:
        reader = csv.DictReader(f_input)
        reader = list(reader)
        writer = csv.DictWriter(f_output, fieldnames=K.FIELDNAMES_SENTIMENT)

        is_first_row = True
        row_count = file_lines_count(reader)

        for i, row in enumerate(reader, 1):
            time, text = row[K.FIELDNAMES[0]], row[K.FIELDNAMES[1]]

            if is_first_row:
                is_first_row = False
                writer.writeheader()
                # create empty row
                sentiment_row = {field: 0 for field in K.FIELDNAMES_SENTIMENT}
            elif sentiment_row["time"] != time or is_last_row(row_count, i):
                # store old row to file
                writer.writerow(sentiment_row)
                # reset row
                sentiment_row = {field: 0 for field in K.FIELDNAMES_SENTIMENT}

            sentiment_row["time"] = time
            sentiment_row["sentiment"] += get_sentiment(text)

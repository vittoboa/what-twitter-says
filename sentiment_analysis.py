import csv

import constants as K


def file_lines_count(file):
    return sum(1 for row in file)


def is_last_row(row_count, current_row):
    return current_row == row_count


def is_team_mentioned(team_name, team_hashtag, text):
    return team_name in text or ("#" + team_hashtag) in text


if __name__ == '__main__':
    team_home_mentions_num, team_away_mentions_num = 0, 0

    with open(K.CLEANED_TWEETS_FILE, 'r', newline='') as f_input, open(K.SENTIMENT_TWEETS_FILE, 'w') as f_output:
        reader = csv.DictReader(f_input)
        reader = list(reader)
        writer = csv.DictWriter(f_output, fieldnames=K.FIELDNAMES_SENTIMENT)

        row_time = None
        is_first_row = True
        row_count = file_lines_count(reader)

        for i, row in enumerate(reader, 1):
            time, text = row[K.FIELDNAMES[0]], row[K.FIELDNAMES[1]]

            if is_first_row:
                row_time = time
                writer.writeheader()
                is_first_row = False
            elif row_time != time or is_last_row(row_count, i):
                writer.writerow({
                    K.FIELDNAMES_SENTIMENT[0]: row_time,
                    K.FIELDNAMES_SENTIMENT[1]: team_home_mentions_num,
                    K.FIELDNAMES_SENTIMENT[2]: team_away_mentions_num
                })

                row_time = time
                team_home_mentions_num, team_away_mentions_num = 0, 0

            if is_team_mentioned(K.TEAM_HOME, K.TEAM_HOME_ABBREVIATION, text):
                team_home_mentions_num += 1
            if is_team_mentioned(K.TEAM_AWAY, K.TEAM_AWAY_ABBREVIATION, text):
                team_away_mentions_num += 1

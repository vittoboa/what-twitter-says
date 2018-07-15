import csv

import constants as K


def is_team_mentioned(team_name, team_hashtag, text):
    return team_name in text or ("#" + team_hashtag) in text


if __name__ == '__main__':
    team_home_mentions_num, team_away_mentions_num = 0, 0

    with open(K.CLEANED_TWEETS_FILE, 'r', newline='') as f_input:
            reader = csv.DictReader(f_input)
            for row in reader:
                time, text = row[K.FIELDNAMES[0]], row[K.FIELDNAMES[1]]
                if is_team_mentioned(K.TEAM_HOME, K.TEAM_HOME_ABBREVIATION, text):
                    team_home_mentions_num += 1
                if is_team_mentioned(K.TEAM_AWAY, K.TEAM_AWAY_ABBREVIATION, text):
                    team_away_mentions_num += 1

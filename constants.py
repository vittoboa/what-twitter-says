KEYWORDS_LIST = [
    "france",
    "fra",
    "croatia",
    "cro",
]
LANGUAGES_LIST = ["en"]
FETCHED_TWEETS_FILE   = "raw_tweets.csv"
CLEANED_TWEETS_FILE   = "cleaned_tweets.csv"
SENTIMENT_TWEETS_FILE = "sentiment_tweets.csv"
WORDS_COUNT_FILE      = "words_count.csv"
FIELDNAMES = ["time", "text"]
SLANG = {
    "ftw": "for the win",
    "gr8": "great",
    "imo": "in my opinion",
    "lol": "laughing out loud",
    "smh": "disappointed",  # Shaking My Head in disappointment
    "smdh": "very disappointed",  # Shaking My Damn Head
    "btw": "by the way",
    "b4": "before",
    "idk": "i don't know"
}

SENTIMENT_THRESHOLD = 0.15
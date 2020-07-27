# what-twitter-says
Three individual scripts to collect, clean and analyze tweets

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python 3](https://www.python.org/downloads/).
From your command line:
```bash
# Clone this repository
$ git clone https://github.com/vittoboa/what-twitter-says

# Go into the repository
$ cd what-twitter-says

# Install the requirements
$ pip3 install -r requirements.txt

# Fill in your Twitter App credentials to config.py 
$ vim config.py

# Run the desidered script in the terminal
$ python3 data_collection.py
$ python3 data_preparation.py
$ python3 sentiment_analysis.py
```

## Built With
This software uses the following open source packages:
- [Tweepy](http://docs.tweepy.org/en/v3.5.0/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)

## Analysis example: 2018 FIFA World Cup Final
Sentiment analysis of Twitter comments:
&nbsp;
<img src="media/sentiment_analysis.jpg" width="100%">
&nbsp;
&nbsp;
Most mentioned players on Twitter:
<img src="media/mentions.png" width="100%">
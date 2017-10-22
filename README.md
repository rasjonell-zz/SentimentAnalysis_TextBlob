# Sentiment Analysis Bot.
Sentiment Analysis Bot that extracts tweets from a given hashtag and labels them according to their negativity level.

## Prerequisites
First, install Ipython:
```
$ sudo apt-get -y install ipython ipython-notebook
```
Next, install Jupyter Notebook
```
$ sudo -H pip install jupyter
```
### Creating a Twitter App

You’ll need to create a Twitter app and you should have your Consumer Key, Consumer Secret, Access Token, and Access Token Secret in hand before beginning this.
### Insatlling Libraries
To install the required libraries type:
```
$ pip install -r requirements.txt
```

## Getting Started

in credentials.py replace the items in single quotes with your unique strings from the Twitter apps website (and keep the single quotes).

## Running The Bot

First, run Jupyter Notebook in the repo's directory by typing:
```
$ jupyter notebook
```
Then, open ```main.py.ipynb``` and click run!


## Useful Links

* [Installing Jupyter Notebook](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-jupyter-notebook-to-run-ipython-on-ubuntu-16-04)
* [Tweepy Docs](http://docs.tweepy.org/en/v3.5.0/)

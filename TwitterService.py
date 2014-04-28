import tweepy
import config
import datetime

class TwitterService:

	def __init__(self):
		consumer_key = config.consumer_key_twitter
		consumer_secret = config.consumer_secret_twitter
		access_token = config.access_token_twitter
		access_token_secret = config.access_token_secret_twitter
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		self.tweepyAPI = tweepy.API(auth)

	def tweet(self, message):
		self.tweepyAPI.update_status(message + ' ' + self.__getStamp())

	def __getStamp(self):
		return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		
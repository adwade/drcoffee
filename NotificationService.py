from flask import Flask
from flask import Response
from TwitterService import TwitterService
from FacebookService import FacebookService
from SmsService import SmsService

class NotificationService:

	def __init__(self):
		self.smsService = SmsService()
		self.facebookService = FacebookService()
		self.twitterService = TwitterService()

	def notifyAll(self, message):
		self.smsService.sendEmail(message)
		self.smsService.sendText(message)
		self.facebookService.postToWall(message)
		self.twitterService.tweet(message)

	def notifySocialServices(self, message):
		self.facebookService.postToWall(message)
		self.twitterService.tweet(message)

	def notifyPersonalServices(self, message):
		self.smsService.sendMail(message)
		self.smsService.sendText(message)

	def notifySpecificService(self, service, message):
		{'facebook': self.facebookService.postToWall(message),
		 'twitter': self.twitterService.tweet(message),
		 'email': self.smsService.sendMail(message),
		 'text': self.smsService.sendText(message),
		 }[service]
	

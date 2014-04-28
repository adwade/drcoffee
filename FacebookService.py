from facepy import utils
from facepy import GraphAPI
import datetime
import config

class FacebookService:

	def __init__(self):
		app_id = config.app_id_facebook
		app_secret = config.app_secret_facebook
		access_token = utils.get_application_access_token(app_id, app_secret)
		self.graphAPI = GraphAPI(access_token)

	def postToWall(self, message):
		self.graphAPI.post('rasberrycoffee/feed', message=message + ' ' + self.__getStamp())

	def __getStamp(self):
		return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
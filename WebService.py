import prop
from flask import Flask
from flask import Response
from NotificationService import NotificationService

class WebService:

	def __init__(self, app):
		self.app = app
		self.notificationService = NotificationService()

	def handleEnableCoffeepot(self, additions):
		if self.__validateCoffeeAdditions(additions) and not prop.isBrewing:
			#Enable coffeepot here
			prop.isBrewing=True
			self.app.logger.info('Coffeepot successfully enabled.')
			self.app.logger.info('Attempting client notification.')
			self.notificationService.notifyAll(prop.startBrewNotification)
			self.app.logger.info('Client successfully notified.')
			return Response(response=prop.startBrewResponse, headers={ 'Safe':'if-user-awake' })
		elif prop.isBrewing:
			self.app.logger.warning('Coffeepot is already brewing!')
			self.app.logger.info('Attempting client notification.')
			self.notificationService.notifyAll(prop.startBrewWhenEnabledNotification)
			self.app.logger.info('Client successfully notified.')
			return Response(response=prop.startBrewWhenEnabledResponse, headers={ 'Safe':'if-user-understands-logic' })
		else:
			self.app.logger.warning('Client attempted to add invalid addition.')
			self.app.logger.info('Attempting client notification.')
			self.notificationService.notifyAll(prop.invalidAdditionNotification)
			self.app.logger.info('Client successfully notified.')
			self.app.logger.critical('(406): CANNOT add requested addition.')
			return Response(response=prop.error406, headers={ 'Safe':'if-user-lactose-tolerant' })

	def __validateCoffeeAdditions(self, additions):
		self.app.logger.info('Validation for additions called.')
		if additions == 'milk-type;Whole-milk':
			prop.isAddingAddition=True
		return additions == 'milk-type;Whole-milk' or additions == ''
		
	def handleDisableCoffeepot(self):
		if not prop.isBrewing:
			self.app.logger.warning('Coffeepot is not brewing!')
			self.app.logger.info('Attempting client notification.')
			self.notificationService.notifyAll(prop.stopBrewWhenDisabledNotification)
			self.app.logger.info('Client successfully notified.')
			return Response(response=prop.stopBrewWhenDisabledResponse, headers={ 'Safe':'if-user-understands-logic' })
		else:
			#Disable coffeepot here
			prop.isBrewing=False
			self.app.logger.info('Coffeepot successfully disabled.')
			self.app.logger.info('Attempting client notification.')
			self.notificationService.notifyAll(prop.stopBrewNotification)
			self.app.logger.info('Client successfully notified.')
			return Response(response=prop.stopBrewResponse, headers={ 'Safe':'if-user-asleep' })

	def handleSayWhen(self):
		if prop.isAddingAddition:
			#Stop adding addition
			prop.isAddingAddtion=False
			self.app.logger.info('Addition successfully stopped.')
			self.app.logger.info('Attempting client notification.')
			self.notificationService.notifyAll(prop.stopAdditionNotification)
			self.app.logger.info('Client successfully notified.')
			return Response(response=prop.stopAdditionResponse, headers={ 'Safe':'if-user-asleep' })
		else:
			self.app.logger.warning('No addition is being added!')
			self.app.logger.info('Attempting client notification.')
			self.notificationService.notifyAll(prop.noAdditionBeingAddedNotification)
			self.app.logger.info('Client successfully notified.')
			return Response(response=prop.noAdditionBeingAddedResponse, headers={ 'Safe':'if-user-asleep' })

	def handleTeapot(self):
		self.app.logger.warning('Client attempted to brew coffee with teapot.')
		self.app.logger.info('Attempting client notification.')
		self.notificationService.notifyAll(prop.teapotNotification)
		self.app.logger.info('Client successfully notified.')
		self.app.logger.critical('(418): CANNOT brew coffee with teapot.')
		return Response(response=prop.error418, headers={ 'Safe':'if-user-competent' })   

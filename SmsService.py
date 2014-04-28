import smtplib
import config

class SmsService:

	def __init__(self):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(config.sms_sender, config.sms_sender_pass)
		self.server = server
	
	def sendEmail(self, message):
		self.server.sendmail(config.sms_sender, 
					 config.sms_recipient_email, 
						 message)

	def sendText(self, message):
		self.server.sendmail(config.sms_sender, 
					 config.sms_recipient_number, 
					 message)


from middleware import MethodRewriteMiddleware
from flask import Flask
from flask import request
from flask import Response
from WebService import WebService


app = Flask(__name__, static_url_path='')
app.wsgi_app = MethodRewriteMiddleware(app.wsgi_app)
webService = WebService(app)


@app.route('/')
def index():
	app.logger.info('Client visited user page.')
	return app.send_static_file('index.html')

@app.route('/brewCoffee', methods=['BREW'])
def brew_coffee():
	brewingDevice = request.headers.get('Brewing-Device')
	coffeeCommand = request.headers.get('Coffee-Command')
	coffeeAdditions = request.headers.get('Accept-Additions')

	if brewingDevice == 'coffeepot' and coffeeCommand == 'start':
		app.logger.info('Client requested coffeepot-enable.')
		return webService.handleEnableCoffeepot(coffeeAdditions)
	elif brewingDevice == 'coffeepot' and coffeeCommand == 'stop':
		app.logger.info('Client requested coffeepot-disable.')
		return webService.handleDisableCoffeepot()
	elif brewingDevice == 'teapot':
		app.logger.warning('Client requested coffee from teapot.')
		return webService.handleTeapot()

@app.route('/getCoffeeProperties', methods=['PROPFIND'])
def get_properties():
	app.logger.info('Client requested coffee properties.')
	return app.send_static_file('coffeemetadata.html')

@app.route('/sayWhen', methods=['WHEN'])
def say_when():
	app.logger.info('Client requested to stop addition.')
	return webService.handleSayWhen()

if __name__ == '__main__':
	app.debug = True
	app.run()


import os
import io

import cherrypy
from genshi.template import TemplateLoader


config = {
	'global': {
		'server.production': True,
		'server.socket_port': int(os.environ.get('PORT', 8080)),
		'server.socket_host': '::0',
		'tools.encode.on': True,
		'tools.encode.encoding': 'utf-8',
		'tools.decode.on': True,
	},
}


loader = TemplateLoader('.')

class Server:
	@cherrypy.expose
	def index(self):
		return self.load_response('welcome')

	@property
	def numbers(self):
		return os.environ['NUMBERS'].split(',')

	@cherrypy.expose
	def authorize_entry(self, RecordingUrl, RecordingDuration, Digits):
		return self.load_response(
			'authorize-entry',
			numbers=self.numbers,
			recording_URL=RecordingUrl,
		)

	def load_response(self, name, **params):
		cherrypy.response.headers['Content-Type'] = 'application/xml'
		return loader.load(name + '.xml').generate(**params).render('xml').encode('utf-8')

	@classmethod
	def run(cls):
		cherrypy.quickstart(cls(), config=config)


if __name__ == '__main__':
	Server.run()

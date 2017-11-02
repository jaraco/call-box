__requires__ = ['cherrypy', 'genshi']

import os

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
	def index(self, **params):
		tmpl = os.environ.get('TECHNIQUE', 'welcome')
		return self.load_response(tmpl, numbers=self.numbers)

	@property
	def numbers(self):
		return list(filter(None, os.environ.get('NUMBERS', '').split(',')))

	@cherrypy.expose
	def authorize_entry(self, RecordingUrl, **params):
		return self.load_response(
			'authorize-entry',
			numbers=self.numbers,
			recording_URL=RecordingUrl,
		)

	def load_response(self, name, **params):
		cherrypy.response.headers['Content-Type'] = 'application/xml'
		tmpl = loader.load(name + '.xml')
		return tmpl.generate(**params).render('xml').encode('utf-8')

	@classmethod
	def run(cls):
		cherrypy.quickstart(cls(), config=config)


if __name__ == '__main__':
	Server.run()

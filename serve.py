import os
import io

import cherrypy


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


class Server:
	@cherrypy.expose
	def index(self):
		cherrypy.headers['Content-Type'] = 'application/xml'
		return self.load_response('welcome')

	def load_response(self, name):
		with io.open(name + '.xml') as strm:
			return strm.read()

	@classmethod
	def run(cls):
		cherrypy.quickstart(cls(), config=config)


if __name__ == '__main__':
	Server.run()

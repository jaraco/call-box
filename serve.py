import os

import cherrypy


config = {
	'global': {
		'server.production': True,
		'server.socket_port': int(os.environ.get('PORT', 8080)),
		'server.socket_host': '127.0.0.1',
		'tools.encode.on': True,
		'tools.encode.encoding': 'utf-8',
		'tools.decode.on': True,
	},
}

class Server:
	@cherrypy.expose
	def index(self):
		return "hello world"

	@classmethod
	def run(cls):
		cherrypy.quickstart(cls(), config=config)


if __name__ == '__main__':
	Server.run()

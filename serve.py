import cherrypy


class Server:
	@cherrypy.expose
	def index(self):
		return "hello world"

	@classmethod
	def run(cls):
		cherrypy.quickstart(cls())


if __name__ == '__main__':
	Server.run()

import cherrypy

class RootServer:
    """ return json with upper case of query """
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def example(self, query=""):
        upper_query = self._big_letter(query)
        if query:
            return {"query": query, "upper_query": upper_query}
        else:
            return {"query": "NO_QUERY"}

    def _big_letter(self, query):
        return str(query).upper()

if __name__ == '__main__':
    server_config={
        'server.socket_host': '127.0.0.1',
        'server.socket_port':8888,
    }
    cherrypy.config.update(server_config)
    cherrypy.quickstart(RootServer())
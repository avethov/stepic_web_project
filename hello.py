import urlparse

def app(environ, start_response):
	params = urlparse.parse_qs(environ["QUERY_STRING"])

	start_response("200 OK", [("Content-Type", "text/plain")])

	return ['%s=%s<br>' % (k, params[k][0]) for k in params]
	

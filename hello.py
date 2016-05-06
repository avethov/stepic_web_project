import urlparse

def wsgi_app(environ, start_response):
	params = urlparse.parse_qs(environ["QUERY_STRING"])

	body = "query strings:\n"
	for k in params.iterkeys():
		body += k + ":\n"
		body += "\n ".join(params[k]) + "\n\n"

	start_response("200 OK",
			[("Content-Type", "text/plain"),
			("Content-Length", str(len(body)))]

	return [body]
	

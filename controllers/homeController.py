def homeController(requestHandler):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-type', 'text/html')
    requestHandler.end_headers()
    requestHandler.wfile.write(b'<h1>Welcome to los pollos hermanos! My name is Gustavo</h1>')

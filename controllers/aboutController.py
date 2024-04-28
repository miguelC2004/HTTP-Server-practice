def aboutController(request_handler):
    request_handler.send_response(200)
    request_handler.send_header('Content-type', 'text/html')
    request_handler.end_headers()
    request_handler.wfile.write(b'<h1>About Us</h1><p>.</p>')

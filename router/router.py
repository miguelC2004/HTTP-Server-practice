from http.server import BaseHTTPRequestHandler
from controllers.home_controller import homeController
from controllers.aboutController import aboutController

class Router(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            '/': homeController,
            '/about': aboutController
        }

        if self.path in routes:
            controller = routes[self.path]
            controller(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

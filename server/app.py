from http.server import HTTPServer
from router.router import Router
from utils.config import load_config

def run(server_class=HTTPServer, handler_class=Router):
    config = load_config()
    server_address = ('', config['PORT'])
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {config["PORT"]}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

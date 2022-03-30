from wsgiref.simple_server import make_server
from main import app

if __name__ == '__main__':
    with make_server('localhost', 8081, app) as httpd:
        print('Serving on port 8081...')

        # Serve until process is killed
        httpd.serve_forever(0.5)

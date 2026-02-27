import threading
import webbrowser

from flask import Flask, send_from_directory

app = Flask(__name__,
            static_folder='../front/static',
            template_folder='../front/pages')

PORT = 5000
HTML_FILE = 'index.html'

@app.route('/')
def index():
    return send_from_directory(app.template_folder, HTML_FILE)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)


def open_browser():
    webbrowser.open(f'http://localhost:{PORT}')


if __name__ == '__main__':
    print(f"Starting server at http://localhost:{PORT}")
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True, port=PORT, host='localhost', use_reloader=False)


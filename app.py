from flask import Flask
from flask_cors import CORS

from controllers import front_controller as fc

app = Flask(__name__)
CORS(app)
fc.route(app)

if __name__ == '__main__':
    app.run(debug=True)

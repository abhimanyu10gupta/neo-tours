import os
from flask import Flask, request, jsonify, abort, current_app
from sqlalchemy import exc
import json
from flask_cors import CORS
import traceback

from .database.models import setup_db
# from .auth.auth import AuthError, requires_auth

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#
app = Flask(__name__)

with app.app_context():
    # within this block, current_app points to app.
    setup_db(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers',
                         'GET, POST, PATCH, DELETE, OPTIONS')
    return response

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/')
def index():
    return "HELLO!!! You are doing it!!!!!"


# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run()

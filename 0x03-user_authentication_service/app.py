#!/usr/bin/env python3
""" End-to-end integration test"""

from auth import Auth
from flask import (Flask,
                   jsonify,
                   request,
                   abort,
                   redirect)

app = Flask(__name__)
AUTH = Auth()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

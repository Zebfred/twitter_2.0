"""Entry point for our twitoff flask app"""

from flask import Flask

app = Flask(__name__)

from app import routes


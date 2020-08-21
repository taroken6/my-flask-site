from flask import Flask

app = Flask(__name__)

from siteblog import routes

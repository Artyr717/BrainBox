from flask import Flask
from app.views import HomeView

app = Flask(__name__)

app.add_url_rule('/', view_func=HomeView.as_view("/"))
app.add_url_rule('/index', view_func=HomeView.as_view("index"))

from flask import Flask
from app.views import HomeView, GeometryView, AlgebraView

app = Flask(__name__)

app.add_url_rule('/', view_func=HomeView.as_view("/"))
app.add_url_rule('/index', view_func=HomeView.as_view("index"))
app.add_url_rule("/geometry", view_func=GeometryView.as_view("geometry"))
app.add_url_rule("/algebra", view_func=AlgebraView.as_view("algebra"))

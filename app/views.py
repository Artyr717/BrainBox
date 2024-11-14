from flask import render_template, request, redirect, url_for
from flask.views import MethodView


class HomeView(MethodView):
    """Класс представления Главной страницы """

    def get(self) -> str:
        return render_template("index.html")

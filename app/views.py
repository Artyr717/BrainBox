from flask import render_template, request, redirect, url_for
from flask.views import MethodView


class HomeView(MethodView):
    """Класс представления Главной страницы """

    def get(self) -> str:
        return render_template("index.html")


class GeometryView(MethodView):
    """Класс представления страницы 'Геометрия' """

    def get(self) -> str:
        class_number = request.args.get('class', default=7, type=int)
        geom_dict = {
            7: "/static/geom7.pdf",
            8: "/static/geom8.pdf",
            9: "/static/geom9.pdf",
            10: "/static/geom10.pdf",
            11: "/static/geom11.pdf"
        }
        return render_template("geom.html", file_path=geom_dict[class_number], class_number=class_number)


class AlgebraView(MethodView):
    """Класс представления страницы 'Алгебра' """

    def get(self) -> str:
        class_number = request.args.get('class', default=7, type=int)
        algebra_dict = {
            7: "/static/algebra7.pdf",
            8: "/static/algebra8.pdf",
            9: "/static/algebra9.pdf",
            10: "/static/algebra10.pdf",
            11: "/static/algebra11.pdf"
        }
        return render_template("algebra.html", file_path=algebra_dict[class_number], class_number=class_number)

class PhysicsView(MethodView):
    """Класс представления страницы 'Физика' """

    def get(self) -> str:
        class_number = request.args.get('class', default=7, type=int)
        phys_dict = {
            7: "/static/phys7.pdf",
            8: "/static/phys8.pdf",
            9: "/static/phys9.pdf",
            10: "/static/phys10.pdf",
            11: "/static/phys11.pdf"
        }
        return render_template("phys.html", file_path=phys_dict[class_number], class_number=class_number)
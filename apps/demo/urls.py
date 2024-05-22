from flask import Blueprint
from flask_restful import Api

from apps.demo import views as data_w

urlpatterns = Blueprint(import_name=__name__, name="data")

api_rest = Api(urlpatterns)

api_rest.add_resource(data_w.DemoApiView, "/demo")

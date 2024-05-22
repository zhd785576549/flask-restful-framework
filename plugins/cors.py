from flask import Flask
from flask_cors import CORS

from core.base import BasePlugin


class CorsPlugin(BasePlugin):

    def init(self, app: Flask):
        CORS(app=app, supports_credentials=True)


cors_plugin = CorsPlugin()

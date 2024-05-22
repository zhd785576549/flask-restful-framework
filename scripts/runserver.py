from argparse import ArgumentParser

from core.base import BaseCommand
from models.user import *


class MigrateCommand(BaseCommand):

    command_name = "runserver"
    helper = "启动一个开发api服务。"

    def add_parser(self, parser: ArgumentParser):
        parser.add_argument("--port", type=int, default=18080, help="Server port.")
        parser.add_argument("--host", type=str, default="0.0.0.0", help="Server host.")
        return parser

    def handle_run(self, **kwargs):
        host = kwargs.get("host")
        port = kwargs.get("port")
        self.app.run(host=host, port=port, debug=True)

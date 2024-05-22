from argparse import ArgumentParser

from core.base import BaseCommand
from models.user import *


class MigrateCommand(BaseCommand):

    command_name = "migrate"
    helper = "迁移数据库表结构。"

    def add_parser(self, parser):
        return parser

    def handle_run(self, **kwargs):
        db_plugin.db.create_all()

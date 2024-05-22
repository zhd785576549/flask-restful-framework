import subprocess
from argparse import ArgumentParser

from core.base import BaseCommand
from utils import funcs


class MigrateCommand(BaseCommand):

    command_name = "runapidoc"
    helper = "生成APIDOC文档。"
    need_init_app = False

    def add_parser(self, parser: ArgumentParser):
        parser.add_argument("--output", type=str, default="../apidoc", help="APIDOC输出路径。")
        return parser

    def handle_run(self, **kwargs):
        project_dir = funcs.get_project_root_path()
        output_dir = kwargs.get("output")
        cmd = f"apidoc -i {project_dir} -o {output_dir}"
        subprocess.call(cmd, shell=True)

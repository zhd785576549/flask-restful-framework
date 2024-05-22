from flask_restful.reqparse import RequestParser


def get_user_list_paginate_validator():
    """分页获取用户列表传参数验证"""

    parser = RequestParser()
    parser.add_argument("page", type=str, default="1", required=False, loaction="args")
    parser.add_argument("page_size", type=str, default="1", required=False, loaction="args")
    return parser

from plugins.db import db_plugin
from models import user as user_m


def select_user_list_paginate(page=1, page_size=20):
    """
    分页筛选用户信息

    :param page: [int] 页码
    :param page_size: [int] 每页个数
    :return:
    """
    query = db_plugin.db.session.query(user_m.UserInfo). \
        filter(user_m.UserInfo.bo_del.is_(False))
    return query.paginate(page=page, per_page=page_size, error_out=False)

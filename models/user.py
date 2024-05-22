from sqlalchemy import Column, BigInteger, Boolean, DateTime, String
from plugins.db import db_plugin
from datetime import datetime


class UserInfo(db_plugin.db.Model):
    __tablename__ = "t_user_info"
    __table_args__ = {
        "comment": "用户表"
    }

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="主键")
    username = Column(String(50), comment="用户名")
    password = Column(String(200), comment="密码")
    nickname = Column(String(50), comment="昵称")
    age = Column(String(5), comment="年龄")
    gender = Column(String(10), comment="性别")
    bo_del = Column(Boolean, default=False, comment="逻辑删除")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

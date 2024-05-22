from marshmallow import Schema, fields


class UserInfoSerializer(Schema):
    id = fields.Integer()
    nickname = fields.String()
    age = fields.String()
    gender = fields.String()

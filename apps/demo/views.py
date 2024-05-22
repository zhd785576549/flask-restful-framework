from utils.resp import RespUtils
from utils.resource import Api
from apps.demo import dbis as demo_d
from apps.demo import validators as demo_v
from apps.demo import serializers as demo_s
from utils import funcs


class DemoApiView(Api):

    def post(self):
        return RespUtils.ok()

    def get(self):
        v = demo_v.get_user_list_paginate_validator()
        args = v.parse_args()
        user_list_p = demo_d.select_user_list_paginate(
            page=funcs.trans_int(args.get("page"), 1),
            page_size=funcs.trans_int(args.get("page_size"), 20)
        )
        return RespUtils.ok({
            "total": user_list_p.total,
            "data_list": demo_s.UserInfoSerializer().dump(user_list_p.items, many=True)
        })

    def api_doc_get(self):
        """
        @api {GET} /api/user/paginate 分页获取用户列表
        @apiVersion 1.0.0
        @apiGroup User

        @apiParam {String} [page="1"] 页码
        @apiParam {String} [page_size="20"] 每页个数

        @apiSuccessExample  成功
        {
            "code": 2000,
            "msg": "ok",
            "data": {
                "total": 100,                               // 总数
                "data_list": [
                    {
                        "id": 10,                           // ID
                        "nickname": "zhangsan",             // 昵称
                        "gender": "1",                      // 性别
                        "age": "20"                         // 年龄
                    }
                ]
            }
        }

        @apiErrorExample 内部错误
        {
            "code": 9999,
            "msg": "Inner error",
            "data": null
        }

        @apiSampleRequest off
        """

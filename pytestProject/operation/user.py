from core.result_base import ResultBase
from common.logger import logger
from api.user import user



def login_user(username, password):
    """
    用户登录
    :param username: 用户名
    :param password: 密码
    :return: 自定义返回结果 result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }
    json_data = {
        "password": password,
        "username": username
    }
    res = user.login_user(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def logout_user(token):
    """
    用户退出登录
    :return: 自定义返回结果result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    res = user.logout_user(headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{}".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("退出登录 == >> 返回结果 == >> {}".format(result.response.text))
    return result





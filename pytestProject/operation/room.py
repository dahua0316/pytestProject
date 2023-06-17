from core.result_base import ResultBase
from common.logger import logger
from api.room import room


def get_room_list(current, size, token):
    """
    获取会议列表
    :param current: 当前页
    :param size: 每页数量
    :param token: 用户token
    :return: 自定义返回结果 result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    params = {
        "current": current,
        "size": size
    }
    res = room.get_room_list(params=params, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("获取会议列表 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def create_room(beginTime, endTime, roomName, sceneId, userNum, token):
    """
    创建会议
    :param beginTime:开始时间
    :param endTime: 结束时间
    :param roomName: 房间名称
    :param sceneId: 场景ID
    :param userNum: 最大用户数
    :return: 自定义返回结果result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    json_data = {
        "beginTime": beginTime,
        "endTime": endTime,
        "roomName": roomName,
        "sceneId": sceneId,
        "userNum": userNum
    }
    res = room.create_room(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("创建会议 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def get_room_detail(roomId, token):
    """
    获取会议详情
    :param roomId: 会议ID
    :param token: 操作token
    :return: 自定义返回结果result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    json_data = {
        "roomId": roomId
    }
    res = room.get_room_detail(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("获取会议详情 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

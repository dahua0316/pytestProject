from core.result_base import ResultBase
from common.logger import logger
from api.ticket import ticket


def get_ticket_list(roomId, current, size, token):
    """
    获取门票列表
    :param roomId: 会议ID
    :param current: 当前页
    :param size: 每页数量
    :return:自定义返回关键字返回结果 result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    params = {
        "roomId": roomId,
        "current": current,
        "size": size
    }
    res = ticket.get_ticket_list(params=params, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "获取门票列表 ==>> 接口返回码是 【{}】,返回信息：{}".format(res.json()["code"],
                                                                            res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("获取门票列表 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def genarate_ticket(expiredTime, roomId, tiketAmount, token):
    """
    门票生成
    :param expiredTime: 过期时间
    :param roomId: 房间Id
    :param tiketAmount: 生成门票数量
    :param token: 操作token
    :return:自定义返回结果result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    json_data = {
        "expiredTime": expiredTime,
        "roomId": roomId,
        "ticketAmount": tiketAmount
    }
    res = ticket.genarate_ticket(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "门票生成 ==>> 接口返回码是 【{}】, 返回信息：{}".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    logger.info("门票生成 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def set_aside_ticket(ticketId, token):
    """
    门票作废
    :param ticketId: 门票Id
    :param token: 操作token
    :return:自定义返回结果
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    res = ticket.set_aside_ticket(ticketId, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "废弃门票 ==>> 接口返回码是 【{}】, 返回信息：{}".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    return result

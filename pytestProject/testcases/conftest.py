import pytest
import os
import allure
from api.user import user
from common.logger import logger
from common.mysql_operate import db
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, loginInfo):
    logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, loginInfo))


@pytest.fixture(scope="function")
def login_fixture():
    username = base_data["init_admin_user"]["username"]
    password = base_data["init_admin_user"]["password"]

    header = {
        "Content-Type": "application/json"
    }
    json_data = {
        "password": password,
        "username": username
    }
    loginInfo = user.login_user(json=json_data, headers=header)
    step_login(username, loginInfo)
    yield loginInfo.json()


@pytest.fixture(scope="function")
def delete_create_room():
    """新建房间前，先删除数据，用例执行之后，再次删除以清理数据"""
    del_sql = base_data["init_sql"]["delete_create_room"]
    db.execute_db(del_sql)
    step_first()
    logger.info("创建房间操作：删除已有房间--准备创建新房间")
    logger.info("执行前置SQL:{}".format(del_sql))
    yield
    db.execute_db(del_sql)
    step_last()
    logger.info("创建房间操作：删除已创建的房间")
    logger.info("执行后置SQL:{}".format(del_sql))


@pytest.fixture(scope="function")
def update_ticket_status():
    """作废门票前，先将门票状态设置为未作废"""
    update_sql = base_data["init_sql"]["updata_ticket_status"]
    db.execute_db(update_sql)
    step_first()
    logger.info("更新门票操作：更新门票状态--准备作废门票")
    logger.info("执行前置SQL:{}".format(update_sql))

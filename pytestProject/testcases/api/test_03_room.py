import pytest
import allure
from operation.room import get_room_list, create_room, get_room_detail
from common.logger import logger
from testcases.conftest import api_data


@allure.step("步骤1 ==>> 获取会议列表")
def step_1():
    logger.info("步骤1 ==>> 获取会议列表")


@allure.step("步骤1 ==>> 创建会议")
def step_2():
    logger.info("步骤1 ==>> 创建会议")


@allure.step("步骤1 ==>> 获取会议详情")
def step_3():
    logger.info("步骤1 ==>> 获取会议详情")


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口进行测试")
@allure.feature("会议模块")
class TestRoom():
    @allure.story("用例--获取会议列表")
    @allure.description("该用例是针对获取会议列表的接口测试")
    @allure.issue("https://www.dahua.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.dahua.com", name="点击跳转到对应用例的链接地址")
    @pytest.mark.parametrize("current, size, except_result, except_code, except_message",
                             api_data["test_get_room_list"])
    def test_get_room_list(self, login_fixture, current, size, except_result, except_code, except_message):
        logger.info("*************** 开始执行用例 ***************")
        userinfo = login_fixture
        result = get_room_list(current, size, userinfo.get("data"))
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{},实际结果：【{}】".format(except_code, result.response.json()["code"]))
        assert result.response.json()["code"] == except_code
        assert except_message in result.message
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--创建会议")
    @allure.description("该用例是针对创建会议的接口测试")
    @allure.issue("https://www.dahua.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.dahua.com", name="点击跳转到对应用例的链接地址")
    @pytest.mark.parametrize("beginTime,endTime,roomName,sceneId,userNum,except_result, except_code, except_message",
                             api_data["test_create_room"])
    @pytest.mark.usefixtures("delete_create_room")
    def test_create_room(self, login_fixture, beginTime, endTime, roomName, sceneId, userNum, except_result,
                         except_code, except_message):
        logger.info("*************** 开始执行用例 ***************")
        userinfo = login_fixture
        result = create_room(beginTime, endTime, roomName, sceneId, userNum, userinfo.get("data"))
        step_2()
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{},实际结果：【{}】".format(except_code, result.response.json()["code"]))
        assert result.response.json()["code"] == except_code
        assert except_message in result.message
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--获取会议详情")
    @allure.description("该用例是针对获取会议详情的接口测试")
    @allure.issue("https://www.dahua.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.dahua.com", name="点击跳转到对应用例的链接地址")
    # @pytest.mark.xfail(reason="xfail示例：预期失败的用例，如存在尚未解决的Bug等")
    @pytest.mark.parametrize("rooId, except_result, except_code, except_message", api_data["test_get_room_datail"])
    def test_get_room_datail(self, login_fixture, rooId, except_result, except_code, except_message):
        logger.info("*************** 开始执行用例 ***************")
        userinfo = login_fixture
        result = get_room_detail(rooId, userinfo.get("data"))
        step_3()
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{},实际结果：【{}】".format(except_code, result.response.json()["code"]))
        assert result.response.json()["code"] == except_code
        assert except_message in result.message
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.skip(reason="skip跳过示例：暂时无法运行该用例")
    def test_xx(self):
        pass


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_room.py"])

import pytest
import allure
from operation.ticket import get_ticket_list, genarate_ticket, set_aside_ticket
from common.logger import logger
from testcases.conftest import api_data
from common.set_time import settime



@allure.step("步骤1 ==>> 获取门票列表")
def step_1():
    logger.info("步骤1 ==>> 获取门票列表")


@allure.step("步骤2 ==>> 门票生成")
def step_2():
    logger.info("步骤2 ==>> 门票生成")


@allure.step("步骤3 ==>> 门票作废")
def step_3():
    logger.info("步骤3 ==>> 门票作废")


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口进行测试")
@allure.feature("门票模块")
class TestTickt():


    @allure.story("用例--获取门票列表")
    @allure.description("该用例是针对获取门票列表的接口测试")
    @allure.issue("https://www.dahua.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.dahua.com", name="点击跳转到对应用例的链接地址")
    @pytest.mark.parametrize("roomId, curuent , size , except_result, except_code, except_message",
                             api_data["test_get_ticket_list"])
    def test_get_ticket_list(self, login_fixture, roomId, curuent, size, except_result, except_code, except_message):
        logger.info("*************** 开始执行用例 ***************")
        userinfo = login_fixture
        result = get_ticket_list(roomId, curuent, size, userinfo.get("data"))
        step_1()
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{},实际结果：【{}】".format(except_code, result.response.json()["code"]))
        assert result.response.json()["code"] == except_code
        assert except_message in result.message
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--生成门票")
    @allure.description("该用例是针对生成门票的接口测试")
    @allure.issue("https://www.dahua.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.dahua.com", name="点击跳转到对应用例的链接地址")
    @pytest.mark.parametrize("expiredTime, roomId , ticketAmount, except_result, except_code, except_message",
                             api_data["test_genarate_ticket"])
    def test_genarate_ticket(self, login_fixture, expiredTime, roomId, ticketAmount, except_result, except_code,
                             except_message):
        logger.info("*************** 开始执行用例 ***************")
        userinfo = login_fixture
        expiredTime = settime.add_time()
        result = genarate_ticket(expiredTime, roomId, ticketAmount, userinfo.get("data"))
        step_2()
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{},实际结果：【{}】".format(except_code, result.response.json()["code"]))
        assert result.response.json()["code"] == except_code
        assert except_message in result.message
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--作废门票")
    @allure.description("该用例是针对作废门票的接口测试")
    @allure.issue("https://www.dahua.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.dahua.com", name="点击跳转到对应用例的链接地址")
    @pytest.mark.parametrize("ticketId, except_result, except_code, except_message",
                             api_data["test_set_aside_ticket"])
    @pytest.mark.usefixtures("update_ticket_status")
    def test_set_aside_ticket(self, login_fixture, ticketId, except_result, except_code, except_message):
        logger.info("*************** 开始执行用例 ***************")
        userinfo = login_fixture
        result = set_aside_ticket(ticketId, userinfo.get("data"))
        step_3()
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{},实际结果：【{}】".format(except_code, result.response.json()["code"]))
        assert result.response.json()["code"] == except_code
        assert except_message in result.message
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_04_ticket.py"])

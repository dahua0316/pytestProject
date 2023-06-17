import pytest
import allure
from operation.user import logout_user
from common.logger import logger
from testcases.conftest import api_data


@allure.step("步骤1 ==>> 退出登录")
def step_1(token):
    logger.info("步骤1 ==>> 退出登录token：{}".format(token))



@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口进行测试")
@allure.feature("用户模块")
class TestUserLogout():

    @allure.story("用例--退出登录")
    @allure.description("该用例是针对退出登录的的接口测试")
    @allure.issue("https://www.dahua.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.dahua.com", name="点击跳转到对应用例的链接地址")
    @allure.title("测试数据：【{except_result},{except_code},{except_message}】")
    @pytest.mark.parametrize("except_result , except_code,except_message", api_data["test_logout_user"])
    def test_logout_user(self, login_fixture, except_result, except_code, except_message):
        logger.info("*************** 开始执行用例 ***************")
        userinfo = login_fixture
        result = logout_user(userinfo.get("data"))
        step_1(userinfo["data"])
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{},实际结果：【{}】".format(except_code, result.response.json()["code"]))
        assert result.response.json()["code"] == except_code
        assert except_message in result.message
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_logout_user.py"])

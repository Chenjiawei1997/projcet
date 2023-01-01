# encoding: utf-8
# Author: 陈家伟
import allure
import pytest


@allure.epic("万集接口自动化测试测试")
class TestAPI:
    a = 8

    @allure.story("获取鉴权码接口")
    @allure.feature("模块名称：登录")
    @allure.title("用例名称：接口登录成功")
    @allure.description("登录")
    @allure.severity(allure.severity_level.BLOCKER)
    # @pytest.mark.smoke
    def test_login(self, base_url):
        allure.dynamic.description("登录接口欧")
        url = "/micro/ent/login"
        all_url = base_url + url
        print(all_url)
        print('登录接口测试用例')
        assert 'http' in all_url
        for a in range(1, 11):
            with allure.step("第" + str(a) + "步：步骤如下："):
                print("执行第" + str(a) + "步")
        # 增加用例附件
        # with open('datas.login_yaml.login.yaml', mode="r") as f:
        #     content = f.read()
        #     allure.attach(body=content, name="用例")

    @allure.feature("模块名称：注册")
    @allure.story("注册接口")
    # @pytest.mark.skipif(a < 10, reason="反例跳过不执行")
    # @pytest.mark.che
    def test_store(self):
        allure.dynamic.title("用例名称，验证接口注册成功")
        print('登录测试1')

    @allure.feature("模块名称：登录1")
    def test_login1(self):
        print('登录测试2')

    @allure.feature("模块名称：登录2")
    def test_login2(self):
        print('登录测试3')

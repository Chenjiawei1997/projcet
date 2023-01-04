# encoding: utf-8
# Author: 陈家伟
from pathlib import Path

import allure
import pytest
from commons.request_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml, read_testcase_yaml
import os

# 无论你在哪里执行，他都是获得当前文件的绝对路径
concurrent_path = str(Path(__file__).parent)


@allure.epic("万集接口自动化测试")
class TestAPI:
    # @allure.story("获取鉴权码接口")
    # @allure.feature("模块名称：登录")
    # # @allure.title("用例名称：接口登录成功")
    # @allure.description("登录")
    # @allure.severity(allure.severity_level.BLOCKER)
    # # @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml(concurrent_path+"\\test_login.yaml"))
    def test_login(self, base_url, caseinfo):
        RequestUtil().standard_yaml_case(base_url, caseinfo)
        # name = caseinfo['name']
        # allure.dynamic.description(name)
        # allure.dynamic.title(name)
        # method = caseinfo['request']['method']
        # url = caseinfo['request']['url']
        # all_url = base_url + url
        # headers = caseinfo['request']['headers']
        # json = caseinfo['request']['json']
        # # validate = caseinfo['validate']
        # res = RequestUtil.sess.request(method=method, url=all_url, json=json, headers=headers, params=None)
        # result = res.json()
        # data = {"access_token": result["data"]["access_token"]}
        # username = {"username": result["data"]["userInfo"]["username"]}
        # # cookies = {"cookies": res.cookies}
        # # print(res.cookies)
        # write_yaml("extract.yaml", username)
        # write_yaml("extract.yaml", data)
        # # write_yaml("extract.yaml", cookies)
        # print(res.json())


    #
    # @allure.feature("模块名称：注册")
    # @allure.story("注册接口")
    # # @pytest.mark.skipif(a < 10, reason="反例跳过不执行")
    # # @pytest.mark.che
    # def test_store(self):
    #     allure.dynamic.title("用例名称，验证接口注册成功")
    #     print('登录测试1')
    #
    # @allure.feature("模块名称：登录1")
    # def test_login1(self):
    #     print('登录测试2')
    #
    # @allure.feature("模块名称：登录2")
    # def test_login2(self):
    #     print('登录测试3')

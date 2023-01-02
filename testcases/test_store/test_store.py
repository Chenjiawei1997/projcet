# encoding: utf-8
# Author: 陈家伟
import allure
import pytest
from commons.request_util import RequestUtil
from commons.yaml_util import write_yaml
from commons.yaml_util import read_yaml


@allure.epic("万集接口自动化测试测试")
class TestStore:
    @allure.feature("模块名称：门店")
    def test_store(self):
        allure.dynamic.title("用例名称，门店接口注册成功")
        allure.dynamic.description("门店列表")
        print("订单")

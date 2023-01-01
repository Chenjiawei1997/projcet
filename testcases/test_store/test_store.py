# encoding: utf-8
# Author: 陈家伟

import allure
@allure.epic("万集接口自动化测试测试")
class Test:
    @allure.feature("模块名称：门店")
    def test_sadd(self):
        allure.dynamic.title("用例名称，门店接口注册成功")
        allure.dynamic.description("门店列表")
        print("订单")
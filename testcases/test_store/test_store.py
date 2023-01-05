# encoding: utf-8
# Author: 陈家伟
from pathlib import Path

import allure
import pytest
from commons.request_util import RequestUtil
from commons.yaml_util import read_yaml, read_testcase_yaml

# 无论你在哪里执行，他都是获得当前文件的绝对路径
concurrent_path = str(Path(__file__).parent)


@allure.epic("万集接口自动化测试测试")
class TestStore:
    @allure.story("获取所有门店接口")
    @allure.feature("模块名称：店铺")
    # @allure.title("用例名称：接口登录成功")
    @allure.description("门店")
    @allure.severity(allure.severity_level.BLOCKER)
    # @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml(concurrent_path + "\\test_store.yaml"))
    def test_store(self, base_url, caseinfo):
        RequestUtil().standard_yaml_case(caseinfo, base_url)




    # # 增加门店
    # def test_add_a_store(self, caseinfo):
    #     pass
    #
    # # 查询添加的门店
    # def test_query_for_added_stores(self, caseinfo):
    #     pass
    #
    # # 删除添加的门店
    # def test_delete_store(self, caseinfo):
    #     pass

    # # 导入门店列表
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml(concurrent_path + "\\test_import_the_store_list.yaml"))
    # def test_import_the_store_list(self, base_url, caseinfo):
    #     url = caseinfo['request']['url']
    #     all_url = base_url + url
    #     method = caseinfo['request']['method']
    #     headers = {
    #         "content - Type": "application/json",
    #         "Authorization": "Bearer " + read_yaml("access_token")
    #     }
    #     data = {
    #         "binary": open(r"I:\projcet\testcases\test_store\导入门店模板 (4).xlsx", mode='rb')
    #     }
    #     res = RequestUtil.sess.request(method=method, url=all_url, files=data, headers=headers)
    #     print(res.json())

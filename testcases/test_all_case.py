# encoding: utf-8
# Author: 陈家伟
import allure
import pytest
from pathlib import Path
import yaml

from commons.request_util import RequestUtil
from commons.ddt_util import read_testcase

# 无论你在哪里执行，他都是获得当前文件的绝对路径
current_path = Path(__file__).parent
# 找到当前所有路径下的yaml文件
yaml_case_list = current_path.glob("**/*.yaml")


@allure.epic("项目名称：万集接口自动化测试")
class TestALLAPI:
    pass


# 创建测试用例的方法：
def create_testcase(yaml_path):
    # 读取yaml
    with open(yaml_path, mode='r', encoding='utf-8') as f:
        caseinfo = yaml.load(f, yaml.FullLoader)

    # 用例
    @pytest.mark.parametrize("caseinfo", read_testcase(yaml_path))
    # @pytest.mark.run(order=1)
    def test_func(self, caseinfo, base_url):
        allure.dynamic.feature(caseinfo['feature'])
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtil().standard_yaml_case(caseinfo, base_url)

    return test_func


for yaml_path in yaml_case_list:
    # yaml 的名字
    yaml_name = yaml_path.name[:-5]
    # 表示在类TestAllApi 中增加一个名字为yaml_name测试用例
    setattr(TestALLAPI, f"test_{yaml_name}", create_testcase(yaml_path))

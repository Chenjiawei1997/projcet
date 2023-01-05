# encoding: utf-8
# Author: 陈家伟
import pytest
from commons.yaml_util import clear_yaml


# 执行之前清空extract_yaml 文件
@pytest.fixture(scope="session", autouse=True)
def clear_extract_yaml():
    clear_yaml()

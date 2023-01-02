# encoding: utf-8
# Author: 陈家伟
import os

import yaml


# 获得项目根路径
def get_object_path():
    return os.getcwd()


# 读取yaml
def read_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, encoding='utf-8', mode='rt') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


# 写yaml
def write_yaml(yaml_path, data):
    with open(get_object_path() + "/" + yaml_path, encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空yaml
def clear_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, encoding='utf-8', mode='wt') as f:
        f.truncate()


# 读取测试用例方法
def read_testcase_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, encoding='utf-8', mode='rt') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value

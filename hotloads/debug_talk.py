# encoding: utf-8
# Author: 陈家伟
import os
import yaml


class DebugTalk:
    # 读取yaml数据
    def read_yaml(self, key):
        with open(os.getcwd() + "/extract.yaml", encoding='utf-8', mode='r') as f:
            value = yaml.load(f, yaml.FullLoader)
            # print("value[key]:%s" % value[key])
            return value[key]

import base64
import hashlib
import os
import time

import rsa
import yaml


class DebugTalk:
    # 读取config.yaml的数据
    # def read_config(self, key):
    #     with open(os.getcwd() + "/config.yaml", encoding="utf-8", mode="r") as f:
    #         value = yaml.load(f, yaml.FullLoader)
    #         return value[key]

    # 读取yaml数据
    def read_yaml(self, key):
        with open(os.getcwd() + "/extract.yaml", encoding='utf-8', mode='r') as f:
            value = yaml.load(f, yaml.FullLoader)
            # print("value[key]:%s" % value[key])
            return value[key]

    # # 读取yaml的数据
    # def read_extract_yaml(self, key):
    #     with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="r") as f:
    #         value = yaml.load(f, yaml.FullLoader)
    #         return value[key]

    # 读取yaml的数据
    def read_extract_yaml3(self, key, index):
        with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="r") as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[key][int(index)]

    # 随机数
    def get_time(self, length):
        return str(int(time.time()))[:length]

    # md5加密
    def md5_encode(self, args):
        # 把变量转化成utf-8的编码格式
        args = str(args).encode("utf-8")
        # md5加密
        md5_value = hashlib.md5(args).hexdigest()
        return md5_value

    # base64加密
    def base64_encode(self, args):
        # 把变量转化成utf-8的编码格式
        args = str(args).encode("utf-8")
        # md5加密
        base64_value = base64.b64encode(args).decode(encoding="utf-8")
        return base64_value

    # rsa加密
    def ras_encode(self, args):
        with open("./hotloads/public.pem") as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        # 把变量转化成utf-8的编码格式
        args = str(args).encode("utf-8")
        # 把字符串加密成byte类型
        byte_value = rsa.encrypt(args, pubkey)
        # 把字节转化成字符串格式
        rsa_value = base64.b64encode(byte_value).decode("utf-8")
        return rsa_value
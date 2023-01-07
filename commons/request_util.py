# encoding: utf-8
# Author: 陈家伟
import ast
import logging
import re
import jsonpath
import requests
import yaml

from io import StringIO
from hotloads.debug_talk import DebugTalk
from commons.yaml_util import write_yaml
from commons.assert_util import assert_result

# 获得日志对象
logger = logging.getLogger(__name__)


class RequestUtil:
    sess = requests.session()

    # 标准化测试用例
    def standard_yaml_case(self, caseinfo, base_url):
        # case_keys = yaml.dump(case_keys)  # 把字典转化成字符串
        logger.info("----------测试用例请求开始----------")
        # 在请求之前调用热加载，通过反射使得yaml文件能够调用python里面的函数
        # 字典转换成字符串
        yaml_str = yaml.dump(caseinfo)
        yaml_str = self.replace_hotload(yaml_str)
        caseinfo = yaml.safe_load(StringIO(yaml_str))
        # 标准化
        case_keys = caseinfo.keys()
        # print(case_keys)
        # 如果后者超级是{'title','request','validate'}的超级是set（set_keys）返回是ture
        if set(case_keys).issuperset({'feature', 'title', 'request', 'validate'}):
            request_keys = caseinfo['request'].keys()
            if set(request_keys).issuperset({'method', 'url'}):
                # print('用例格式正确')
                # 处理url
                caseinfo['request']['url'] = base_url + caseinfo['request']['url']
                # 加入日志
                logger.info("用例标题：%s" % caseinfo['title'])
                logger.info("用例方式：%s" % caseinfo['request']['method'])
                logger.info("用例路径：%s" % caseinfo['request']['url'])
                if set(request_keys).issuperset({"headers"}):
                    logger.info("请求头部: %s" % caseinfo["request"]["headers"])
                # 处理files
                for key, value in caseinfo['request'].items():
                    if key == "params":
                        logger.info("用例params参数：%s" % caseinfo['request']['params'])
                    elif key == "data":
                        logger.info("用例data参数：%s" % caseinfo['request']['data'])
                    elif key == "json":
                        logger.info("用例json参数：%s" % caseinfo['request']['json'])
                    # print(key, value)
                    if key == "files":
                        logger.info("用例files参数：%s" % caseinfo['request']['files'])
                        for file_key, file_value in dict(value).items():
                            print(file_key, file_value)
                            value[file_key] = open(file_value, "rb")

                # 发送请求
                res = self.send_all_request(**caseinfo['request'])
                logger.info("预期结果: %s" % caseinfo["validate"])
                logger.info("实际结果: %s" % res.text.rstrip('\n'))
                # 提取中间变量
                self.extract_yaml_value(caseinfo, res)
                # 断言封装
                if caseinfo['validate']:
                    assert_result(caseinfo['validate'], res)
                logger.info("接口测试通过!")
                logger.info("----------测试用例请求结束----------\n")
            else:
                print("Yaml中request目录下必须包含method，url")
                logger.info("----------测试用例请求结束----------\n")
            # print(request_keys)
        else:
            print("Yaml一级目录必须包含feature、title、request、validate")
            logger.info("----------测试用例请求结束----------\n")

    # 统一封装请求路径
    def send_all_request(self, method, url, **kwargs):
        res = RequestUtil.sess.request(method, url, **kwargs)
        # print(res.json())
        return res

    def extract_yaml_value(self, caseinfo, res):
        if "extract" in caseinfo.keys():
            for key, value in caseinfo["extract"].items():
                # 正则提取
                if "(.*?)" in value or "(.+?)" in value:
                    zz_value = re.findall(value, res.text)
                    if len(zz_value) == 0:
                        print("没有提取到值")
                    else:
                        if len(zz_value) == 1:
                            data = {key: zz_value[0]}
                            write_yaml(data)
                            # print('提取到的值为', data)
                            # 指提取到一个值
                        else:
                            data = {key: zz_value}
                            write_yaml(data)
                            # print('提取到的值为', data)
                            # 提取到多个值
                else:
                    js_value = jsonpath.jsonpath(res.json(), value)
                    if js_value:
                        if len(js_value) == 1:
                            # 值提取到一个值
                            data = {key: js_value[0]}
                            write_yaml(data)
                            # print('提取到的值为', data)
                        else:
                            data = {key: js_value}
                            write_yaml(data)
                            # print('提取到的值为', data)

    # 热加载 对httprunner了解的话 通过反射
    def replace_hotload(self, yaml_str):
        regexp = "\\$\\{(.*?)\\((.*?)\\)}"
        # print(yaml_str)
        fun_list = re.findall(regexp, yaml_str)
        # print("fun_list:%s" % fun_list)
        for f in fun_list:
            # 如果他的参数不等于他的字符串代表有参数 ，否则
            if f[1] == "":  # 有参数
                new_value = getattr(DebugTalk(), f[0])()
            else:  # 没有参数
                new_value = getattr(DebugTalk(), f[0])(*f[1].split(","))
            # print('new_value:%s' % new_value)
            oldstr = "${" + f[0] + "(" + f[1] + ")}"  # 拼接旧值
            yaml_str = yaml_str.replace(oldstr, str(new_value))
        return yaml_str

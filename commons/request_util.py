# encoding: utf-8
# Author: 陈家伟
import requests


class RequestUtil:
    sess = requests.session()

    # 标准化测试用例
    def standard_yaml_case(self, caseinfo, baseurl):
        case_keys = caseinfo.keys()
        print(case_keys)
        # 如果后者超级是{'title','request','validate'}的超级是set（set_keys）返回是ture
        if set(case_keys).issuperset({'title', 'request', 'validate'}):
            pass
        else:
            print("Yaml一级目录必须包含title、request、validate")

    # 统一封装请求路径
    def send_all_request(self, method, url, **kwargs):
        for key, value in kwargs.items():
            print(key, value)
            if key == "files":
                for file_key, file_value in dict(value).items():
                    # print(file_key, file_value)
                    value[file_key] = open(file_value, "rb")

        res = RequestUtil.sess.request(method, url, **kwargs)
        return res

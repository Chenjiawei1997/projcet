# encoding: utf-8
# Author: 陈家伟
import requests


class RequestUtil:
    sess = requests.session()

    # 统一封装请求路径
    def send_all_request(self, method, url, **kwargs):
        res = RequestUtil.sess.request(method, url, **kwargs)
        return res

# encoding: utf-8
# Author: 陈家伟
import pytest


class TestAPI:
    a = 8

    @pytest.mark.smoke
    def test_login(self):
        print('登录测试')

    @pytest.mark.skipif(a < 10, reason="反例跳过不执行")
    @pytest.mark.che
    def test_store(self):
        print('登录测试1')

    def test_login1(self):
        print('登录测试2')

    def test_login2(self):
        print('登录测试3')

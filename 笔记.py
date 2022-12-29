

# # @pytest.fixtrue()一般会和conftest.py文件一起使用
#
# # yield 和return 都表示返回数据的意思
# # 区分：yield 可以返回多次以及多个数据，return只会返回一次，return之后不能接代码
# 1、conftest.py文件是单独存放的，@pytest.fixture()的方法。共享之前配置
# 2.conftest.py在使用方法时不需要导入的，可以直接使用
# 3、

# 新建一个公共文件common

# '''
# 接口：
# -----------------------------------------------------------
# def get(url, params=None, **kwargs):
# url：接口地址
# params：参数
# **kwargs：可变长度的字典
# -----------------------------------------------------------
# def post(url, data=None, json=None, **kwargs):
# url：接口地址
# data：参数（表单--x-www-from-urlencoded）
# json：参数（json---application/json）
#     postman四种传参方式：
#     1、from-data(既有表单也有文件上传) files文件上传
#     2、x-www-urlencoded（纯表单）  data
#     3、raw(json)(传json格式的参数)  json
#     4、binary（application/octrent-stream）：（二进制文件） data
# **kwargs：可变长度的字典
# ------------------------------------------------------------
# def put(url, data=None, **kwargs):
# url：接口地址
# data：参数
# **kwargs：可变长度的字典
# ------------------------------------------------------------
# def delete(url, **kwargs):
# url：接口地址
# **kwargs：可变长度的字典
# ------------------------------------------------------------
# ****底层调用的都是同一种方法 request
# request第一层
# req = requests.request('GET', 'https://httpbin.org/get')
#
# requests.request()调用的是session.request方法
# 创建了一个session对象，调用了这个方法
#    return session.request(method=method, url=url, **kwargs)
#
#
# def request(
#         self,
#         method,         请求方式
#         url,            请求路径
#         params=None,    params参数
#         data=None,      data参数
#         headers=None,   请求头
#         cookies=None,   cookies信息
#         files=None,     文件上传
#         auth=None,      鉴权
#         timeout=None,   超时
#         allow_redirects=True,       重定向
#         proxies=None,               设置代理
#         hooks=None,                 钩子
#         stream=None,                文件下载
#         verify=None,                证书验证
#         cert=None,                  CA证书
#         json=None,                  json参数
#     ):
#
# requests.request()和session.request()的区别：
# 前者每个请求都是独立的，后者会自动关联所有的请求cookie信息
# ------------------------------------------------------------
#
# Requests响应部分：
# res.text    返回字符串形式的结果
# res.json()  返回字典形式的结果
# res.content()   返回字节类型的结果
# res.status_code 返回状态码
# res.reason      返回状态信息
# res.cookie      返回cookie信息
# res.encoding    返回编码格式
# res.headers     返回响应头
# res.request.xxx 得到的请求数据
#
# ----------------------------------------------------------
# ****为什么封装请求？
# 1、去除重复代码
# 2、实现统一的异常处理以及日志监控
# ------------------------------------------------------------
# ***jsonpath提取器实现关联
# jsonpath.jsonpath() 返回一个列表，通过下标取值，没有找到返回None
#
'''
jsonpath表达式基本格式规范
    $ 表示根节点，也是所有jsonpath表达式的开始
    . 表示获取子节点
    .. 表示获取所有符合条件的内容
    * 代表所有的元素节点
    [] 表示迭代器的标示（可以用于处理下标等情况）
    [,] 表示多个结果的选择
    ？() 表示过滤操作
    @ 表示当前节点
'''

'''
引入pytest
作用：
1、发现用例：默认发现用例的规则
    模块名必须以test_开头或者_test结尾
    测试类必须以Test开头
    测试方法必须test_开头
2、执行用例
3、判断结果
4、生成报告
二、pytest用例管理框架介绍：
pytest 本身
pytest-html 生成html报告
pytest-xdist 多线程
pytest -ordering 控制用例的执行顺序
pytest -rerunfailures 失败用例重跑 
pytest -base -url  基础路径
allure -pytest  生成allure报告 

# ------------------------------------------------------------
3/通过配置文件pytest.ini 来改变以及执行用例
addopts 配置参数 = -vs 输入更加详细的信息
                -vs -m “smoke” 只执行冒烟用例
testpaths 改变用例的查找规则 = ./testcases  当前目录下
python_files = test_*.py    改变模块查找规则   有中文情况下要改为GBK
python_classes = Test*  改变类的查找规则
python_functions = test_*   改变函数的查找规则
maekers = smoke：冒烟测试   标记

4、pytest用例管理的前后置（固件，夹具）
用例之前 用例之后做一些操作 
def setup 用例之前
def teardown 用例之后
装饰器：
    原有的基础上加装一些东西去强化一些业务
@pytest.fixtrue(scope="作用域"，params='参数化'，autouse="自动执行",ids="参数别名",name=”别名“)
# ------------------------------------------------------------
日志 【pytest】配置信息
log_cli = true  
指定日志级别，该级别的日志记录将被打印到控制台 
log_cli_level = info
格式化日志
log_format = %(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s
log_date_format = %Y-%M-%D %H:%M:%S
格式化日志时间
log_file = ./logs.log
输出日志搭配指定目录
# ------------------------------------------------------------
yaml 用例基础架构
-
 feature: 模块
 story： 接口
 title： 用例标题
 request： 
    method：请求方式
    url： 请求路径
    headers：请求头
    params/data/json/files:参数
 vilidate： 断言
为空就是null

# ------------------------------------------------------------
. 代表当前所在目录

.. 代表当前所在目录的父目录

./ 代表当前所在目录下的某个文件夹或文件

../ 代表当前所在目录的父目录下的某个文件夹或文件
# ------------------------------------------------------------
@pytest.mark.parameteize(args_name,args_value)
args_name:参数的名称
args_value:参数


# ------------------------------------------------------------
GIT：
什么是版本控制？
    为了知道版本的差异，为了区分准确的版本，需要进行版本的控制

了解GIT： 是一个版本的控制工具
1、记录项目的变更历史
2、显示版本的差异
3、切换任意的版本
4、支持多个分支的分工推进，后期分支合并
5、我们可以为版本标记tag
验证安装效果：
git --version

配置基本信息：
git config --global user.name chenjiawei
git config --global user.email 1034672435@qq.com
验证配置是否有效：
    查看编辑信息：git config --global -e
git用法：
git 是以仓库为单位的
    要先创建仓库，不同的仓库之间相互隔离
仓库分两种：
1、本地    存储在文件夹中
2、远程    存储在互联网中
使用流程：
    初级流程：
        1、从远程克隆一个仓库到本地git clone
        2、在本地修改代码，完成之后进行提交 Commit
        3、从本地推送到远程 push
    
    中级使用流程：
        1、从远程克隆一个仓库到本地git clone
        2、在本地创建分支 
        3、在分支中修改代码，完成之后进行提交 Commit
        4、从远程拉取最新代码 Pull
        5、在本地合并分支
        6、从本地推送到远程 push
        
git使用实操：
1、创建远程仓库
    国内远程仓库，gitee国外github
2、记录仓库网址
3、克隆仓库网址
4、本地修改代码
5、提交代码 

# ------------------------------------------------------------


# ------------------------------------------------------------


# ------------------------------------------------------------


# ------------------------------------------------------------


# ------------------------------------------------------------


# ------------------------------------------------------------


# ------------------------------------------------------------


# ------------------------------------------------------------



# ------------------------------------------------------------
# '''
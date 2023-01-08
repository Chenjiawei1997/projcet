import logging
import jsonpath
# 获得日志对象
from commons.mysql_util import execute_sql

logger = logging.getLogger(__name__)


# 总断言方法
def assert_result(validate, res):
    for key, value in validate.items():
        if key == "codes":
            codes_assert(value, res.json()['code'])
            # codes_assert(value, res.status_code)
        elif key == "equals":
            equals_assert(value, res.json())
        elif key == "contains":
            contains_assert(value, res.json())
        elif key == "databases":
            db_assert(value, res.json())
            # print("数据库断言")
        else:
            logger.info("不支持的断言方式")


# 断言日志
def raise_assert_error(msg):
    logger.error(msg + "")
    logger.info("----------测试用例*异常*结束----------\n")
    raise AssertionError(msg)


# 断言状态码
def codes_assert(yq_code, sj_code):
    if yq_code != sj_code:
        raise_assert_error("codes状态码断言失败, 预期结果: " + str(yq_code) + ",实际结果: " + str(sj_code) + "")
    else:
        print("codes状态码断言成功, 预期结果: " + str(yq_code) + ",实际结果: " + str(sj_code) + "")


# 相等断言
def equals_assert(yq_value, sj_json_value):
    for key, value in yq_value.items():
        list_result = jsonpath.jsonpath(sj_json_value, "$..%s" % key)
        if list_result:
            if value not in list_result:
                raise_assert_error("equals断言失败：" + str(key) + " 不等于 " + str(value) + "")
        # else:
        #     raise_assert_error("equals断言失败: 返回结果中没有:" + str(key) + "")
            else:
                print(("equals断言成功：" + str(key) + " 等于 " + str(value) + ""))
        # if list_result:
        #     if value in list_result:
        #         print(("equals断言成功：" + str(key) + " 等于 " + str(value) + ""))


# 包含断言
def contains_assert(yq_value, sj_text_value):
    if str(yq_value) not in sj_text_value:
        raise_assert_error("contains断言失败: 返回结果中不包含" + str(yq_value) + "")
    # else:
    #     print("contains断言成功: 返回结果中包含" + str(yq_value) + "")


# 数据库断言
def db_assert(yq_value, sj_json_value):
    for key, sql in yq_value.items():
        # print(key, sql)
        lists = jsonpath.jsonpath(sj_json_value, "$..%s" % key)
        if lists:
            try:
                select_result = execute_sql(sql)
            except:
                raise_assert_error("databases断言失败: SQL查询异常！请检查SQL语句！")
            #         print("databases断言失败: SQL查询异常！请检查SQL语句！")
            else:
                #         # 如果select_result的长度为0代表SQL没有查询到值
                if len(select_result) == 0:
                    raise_assert_error("databases断言失败: SQL查询没有结果返回！")
                else:
                    # print("预期list:%s" % lists)
                    # print("实际数据库查询select_result:%s" % select_result)
                    print("databases断言成功: 预期结果" + str(select_result[0]) + "等于SQL查询的实际结果" + str(
                        lists[0]) + "！")
                    if str(lists[0]) not in select_result[0]:
                        raise_assert_error(
                            "databases断言失败: 预期结果" + str(select_result[0]) + "不等于SQL查询的实际结果" + str(
                                lists[0]) + "！")
        else:
            # raise_assert_error("databases断言失败: 返回结果中没有:" + str(key) + "")
            raise_assert_error("databases断言失败: 返回结果中没有:" + str(key) + "")
            # print("databases断言失败: 返回结果中没有:" + str(key) + "")

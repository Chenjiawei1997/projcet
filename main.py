# encoding: UTF-8
# 陈家伟
import time
import os
import pytest

if __name__ == '__main__':
    pytest.main(['-vs'])
    # pytest.main(['-vs ./test'])
    # pytest.main(['-vs testcases/test_all_case.py::TestALLAPI::test_A_addOrUpdate.yaml[caseinfo0]'])
    times = time.time()
    # print((times))
    # files_name = "./Reports/report_" + str(int(times))
    # # # # # # os.mkdir(files_name)
    # # # # # time.sleep(3)
    # os.system("allure generate ./temps -o "+files_name+" --clean")




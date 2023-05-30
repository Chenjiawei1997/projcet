# encoding: utf-8
# Author: 陈家伟

from pathlib import Path
from iniconfig import IniConfig


def load_ini():
    '''
    :return: 获取公共参数
    '''
    path = Path("./pytest.ini")
    if not path.exists():
        return {}
    # 判断[apitest]是否存在
    ini = IniConfig("../pytest.ini")
    if "apitest" not in ini:
        return {}
    return dict(ini['apitest'].items())


if __name__ == '__main__':
    print(load_ini())
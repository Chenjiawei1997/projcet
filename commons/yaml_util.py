# encoding: utf-8
# Author: 陈家伟
import yaml


def read_yaml(yaml_path):
    with open(yaml_path, encoding='utf-8', mode='rt') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


if __name__ == '__main__':
    print(read_yaml("I:\projcet\datas\login_yaml\login.yaml"))

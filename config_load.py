# -*- coding: utf-8 -*-

import configparser

def load_conf(conf_name='spider.conf'):
    """
    读取配置文件
    """
    config = configparser.ConfigParser()
    config.read(conf_name, encoding='utf-8')
    return config
    
if __name__=='__main__':
    load_conf()
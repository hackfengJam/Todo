#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"

from fabric.api import *

env.hosts = ['192.168.10.74']
env.user = 'sbin'
env.password = '123456'


def hello():
    print 'hello world'


def deploy():
    with cd('/home/sbin/Todo'):
        run('git pull')
        sudo('supervisorctl restart todo')
        sudo('supervisorctl status')

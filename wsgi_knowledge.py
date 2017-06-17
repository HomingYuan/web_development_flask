#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Homing
@software: PyCharm Community Edition
@file: wsgi_knowledge.py
@time: 2017/6/17 10:00
"""

from eventlet import wsgi
import eventlet


def hello(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World!\r\n']
wsgi.server(eventlet.listen(('127.0.0.1', 8090)), hello)










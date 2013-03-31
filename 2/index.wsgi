#!/usr/bin/env python
# coding: utf-8
import web
import sae
from config.url import urls
import os
import sys
app_root = os.path.dirname(__file__)

# 两者取其一
sys.path.insert(0, os.path.join(app_root, 'virtualenv.bundle'))
#是否具有调试功能
web.config.debug = True
app = web.application(urls, globals())
application = sae.create_wsgi_app(app.wsgifunc())



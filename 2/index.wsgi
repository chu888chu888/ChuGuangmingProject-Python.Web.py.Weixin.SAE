#!/usr/bin/env python
# coding: utf-8
import web
import sae
from config.url import urls

#是否具有调试功能
web.config.debug = True
app = web.application(urls, globals())
application = sae.create_wsgi_app(app.wsgifunc())



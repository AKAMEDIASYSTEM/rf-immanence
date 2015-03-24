#!/usr/bin/env python
# tuned-resonator
# experiments with google physical-web mdns broadcast

import tornado.ioloop
import tornado.web
from handlers.BrowserHandler import BrowserHandler
from handlers.ApiHandler import ApiHandler
import redis
# from handlers.APIHandler import APIHandler

db = redis.StrictRedis(host='localhost', port=6379, db=1)

settings = dict(
    #template_path=os.path.join(os.path.pardir(__file__), "templates"),
    # template_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'../', 'templates')),
    # static_path=os.path.abspath(os.path.join(os.path.dirname( __file__ ),'../', "static")),
    debug=True
)

'''
API - should take as query a date or date range (like, X mins into the past)
should output json in a good format, i have no idea what that looks like

rf-index - main browse-to page of rf-immanence, shows latest heatmap and some explanatory text



'''
application = tornado.web.Application([
    (r"/api", ApiHandler),# this should serve out json scan results
    (r"/", BrowserHandler),
], db=db, **settings)

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
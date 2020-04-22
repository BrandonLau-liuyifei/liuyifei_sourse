# -*- encoding:utf-8 -*-
import tornado.ioloop
import tornado.web

class DistHdl(tornado.web.RequestHandler):
    def get(self):
        self.write("被转向的目的页面！")

class SrcHdl(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/dist')

app = tornado.web.Application([
    (r'/dist',DistHdl),
    (r'/src',SrcHdl),
    (r'/rdrt',tornado.web.RedirectHandler,{'url':'/src'})
    ])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

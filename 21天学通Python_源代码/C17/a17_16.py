# -*- encoding:utf-8 -*-
import tornado.ioloop
import tornado.web

class SttHdl(tornado.web.RequestHandler):
    def get(self):
        self.write("<img src='/static/torn.jpg' />")

app = tornado.web.Application([
    (r'/stt',SttHdl),
    ],static_path='./static')

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

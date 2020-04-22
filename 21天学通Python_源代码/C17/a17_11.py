# -*- encoding:utf-8 -*-
import tornado.ioloop
import tornado.web

class MainHdl(tornado.web.RequestHandler):
    def get(self):
        self.write('你好，我是Tornado!')

app = tornado.web.Application([
    (r'/',MainHdl),
    ],debug=True)

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

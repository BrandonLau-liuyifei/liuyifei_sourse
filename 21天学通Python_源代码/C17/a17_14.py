# -*- encoding:utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.escape

class ScookHdl(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie('odn_cookie',tornado.escape.url_escape("未加密COOKIE串"))
        self.set_secure_cookie('scr_cookie',"加密SCURE_COOKIE串")
        self.write("<a href='/gcook'>查看设置的COOKIE</a>")

class GcookHdl(tornado.web.RequestHandler):
    def get(self):
        odn_cookie = tornado.escape.url_unescape(self.get_cookie('odn_cookie'))
        scr_cookie = self.get_secure_cookie('scr_cookie').decode('utf-8')
        self.write("普通COOKIE:%s,<br/>安全COOKIE:%s" % (odn_cookie,scr_cookie))

app = tornado.web.Application([
    (r'/scook',ScookHdl),
    (r'/gcook',GcookHdl),
    ],cookie_secret='abcddddkdk##$$34323sdDsdfdsf#23')

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

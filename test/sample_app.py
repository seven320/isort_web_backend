# encoding: utf-8

import json 
import falcon

class AppResource(object):
    def on_get(self, req, resp):
        msg = {
            "message":"falcon is fine!!"
        }
        resp.body = json.dumps(msg)

app = falcon.API()
app.add_route("/", AppResource())

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 3000, app)
    httpd.serve_forever()


    
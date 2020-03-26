# encoding: utf-8

import json 
import falcon

class AppResource(object):
    def on_get(self, req, resp):
        """Handles GET requests """
        msg = {
            "message":"hello falcon"
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(msg)

    def on_post(self, req, res):
        msg = {
            "message":"import numpy as np\n\nimport hoge"
        }
        res.body = json.dumps(msg)

def create_app():
    app = falcon.API()
    app.add_route("/", AppResource())

    return app

if __name__ == "__main__":
    from wsgiref import simple_server

    app = create_app()
    httpd = simple_server.make_server("127.0.0.1", 3000, app)
    httpd.serve_forever()
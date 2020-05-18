# encoding: utf-8

import json
import falcon
from isort import SortImports

class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods','GET, POST') # 動作していいmethodを定義
        resp.set_header('Access-Control-Allow-Headers','*')

def sort_libraries(libraries):
    path = "sorted_file"
    with open(path, mode = "w") as f:
        f.writelines(libraries)
    SortImports("sorted_file")
    with open(path, mode = "r") as f:
        sorted_doc = f.read()
    sorted_doc = sorted_doc.rstrip("\n")
    return sorted_doc

class AppResource(object):
    def on_get(self, req, resp):
        """Handles GET requests """
        msg = {
            "message":"Hello Pisort"
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(msg)

    def on_post(self, req, res):
        doc = json.loads(req.bounded_stream.read())

        try: 
            message = doc["message"]
        except:
            raise falcon.HTTPBadRequest()

        sorted_doc = sort_libraries(doc["message"])

        msg = {
            "message": sorted_doc
        }
        res.body = json.dumps(msg)

def create_app():
    app = falcon.API(middleware = [HandleCORS()])
    app.add_route("/", AppResource())

    return app

if __name__ == "__main__":
    from wsgiref import simple_server

    app = create_app()
    httpd = simple_server.make_server("0.0.0.0", 8080, app)
    httpd.serve_forever()

# encoding: utf-8

import os
import json
import falcon
from isort import SortImports
from dotenv import load_dotenv

if os.path.exists("/env/.env"):
    load_dotenv("/env/.env")
elif os.path.exists("env/.env"):
    load_dotenv("env/.env")
else:
    print("error doesn't exist .env path")

API_KEY = os.environ.get("api_key")


class HandleCORS(object):
    def process_request(self, req, resp):
        origin = req.get_header("Origin")
        if origin is not None and origin == "https://www.pisort.denden.app":
            resp.set_header("Access-Control-Allow-Origin", origin)
            resp.set_header("Access-Control-Allow-Methods", "GET, POST")
            resp.set_header("Access-Control-Allow-Headers", "*")


def sort_libraries(libraries):
    path = "sorted_file"
    with open(path, mode="w") as f:
        f.writelines(libraries)
    SortImports("sorted_file")
    with open(path, mode="r") as f:
        sorted_doc = f.read()
    sorted_doc = sorted_doc.rstrip("\n")
    return sorted_doc


class AppResource(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def on_get(self, req, resp):
        if req.get_header("Authorization") != f"Bearer {self.api_key}":
            raise falcon.HTTPUnauthorized()
        resp.status = falcon.HTTP_200  # ステータスコード200を設定

        msg = {"message": "Hello Pisort"}
        resp.body = json.dumps(msg)

    def on_post(self, req, res):
        if req.get_header("Authorization") != f"Bearer {self.api_key}":
            raise falcon.HTTPUnauthorized()
        doc = json.loads(req.bounded_stream.read())
        try:
            message = doc["message"]
        except:
            raise falcon.HTTPBadRequest()

        sorted_doc = sort_libraries(doc["message"])

        msg = {"message": sorted_doc}
        res.body = json.dumps(msg)


def create_app(api_key):
    app = falcon.API(middleware=[HandleCORS()])
    app.add_route("/", AppResource(api_key))

    return app


if __name__ == "__main__":
    from wsgiref import simple_server

    app = create_app(API_KEY)
    httpd = simple_server.make_server("0.0.0.0", 8080, app)
    httpd.serve_forever()

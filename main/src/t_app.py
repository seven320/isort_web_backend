# -------
# unittest
# --------

import unittest
import falcon
from falcon import testing
import app
import json

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()

        self.app = app.create_app()

class TestMyApp(MyTestCase):
    def test_get_message(self):
        doc = {u'message': u'hello Pisort'}
        result = self.simulate_get("/")
        self.assertEqual(result.json, doc)

    def test_post_message(self):
        body = {u'message': u'hello post'}
        headers = {"Content-Type": "application/json"}
        result = self.simulate_post("/", body = json.dumps(body), headers = headers)

        doc = {u'message':u'hello post'}
        self.assertEqual(result.json, doc)

    def test_post_sort(self):
        body = {u'message':(
        u"# encoding: utf-8\n"
        "import hometamon\n"
        "import numpy as np\n"
        "import json\n"
        "import os, sys\n"
        "import cv2")}
        headers = {"Content-Type": "application/json"}

        result = self.simulate_post("/", body = json.dumps(body), headers = headers)
        doc = {u'message':(
        u'# encoding: utf-8\n'
        'import os\n'
        'import sys\n'
        'import json\n\n'
        'import cv2\n'
        'import numpy as np\n\n'
        'import hometamon')}
        self.assertEqual(result.json, doc)

    def test_post_null(self):
        body = {u'message':()}
        headers = {}
        result = self.simulate_post("/", body = json.dumps(body), headers = headers)

        doc = {u'message':('')}
        self.assertEqual(result.json, doc)

    def test_post_bad_request(self):
        body = {}
        result = self.simulate_post("/", body = json.dumps(body))
        print(result)
        self.assertEqual(result.status, "400 Bad Request")

if __name__ == "__main__":
    unittest.main()

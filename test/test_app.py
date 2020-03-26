# -------
# unittest
# --------

import unittest
import falcon
from falcon import testing
import sample_app
import json

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()

        self.app = sample_app.create_app()

class TestMyApp(MyTestCase):
    def test_get_message(self):
        doc = {u'message': u'hello falcon'}
        result = self.simulate_get("/")
        self.assertEqual(result.json, doc)

    def test_post_message(self):
        body = {u'message': u'import hoge\nimport numpy as np'}
        headers = {"Content-Type": "application/json"}
        result = self.simulate_post("/", body = json.dumps(body), headers = headers)

        doc = {u'message':u'import numpy as np\n\nimport hoge\n'}
        self.assertEqual(result.json, doc)

    def test_sort(self):
        body = {u'message':u'import json\nimport falcon\nfrom isort import SortImports'}
        headers = {"Content-Type": "application/json"}
        result = self.simulate_post("/", body = json.dumps(body), headers = headers)

        doc = {u'message': u'import json\n\nimport falcon\nfrom isort import SortImports\n'}
        self.assertEqual(result.json, doc)

        
if __name__ == "__main__":
    unittest.main()
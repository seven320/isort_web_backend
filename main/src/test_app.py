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
        doc = {u'message': u'hello falcon'}
        result = self.simulate_get("/")
        self.assertEqual(result.json, doc)

    def test_post_message(self):
        body = {u'message': u'hello post'}
        headers = {"Content-Type": "application/json"}
        result = self.simulate_post("/", body = json.dumps(body), headers = headers)

        doc = {u'message':u'hello post\n'}
        self.assertEqual(result.json, doc)

    def test_post_sort(self):
        body = {u'message':(
        u"# encoding: utf-8\n"
        "import hometamon\n"
        "import numpy as np\n"
        "import json\n"
        "import os, sys")}
        headers = {"Content-Type": "application/json"}

        result = self.simulate_post("/", body = json.dumps(body), headers = headers)
        doc = {u'message':(
        u'# encoding: utf-8\n'
        '# Standard Library\n'
        'import os\n'
        'import sys\n'
        'import json\n\n'
        '# Third Party Library\n'
        'import numpy as np\n\n'
        '# My Stuff\n'
        'import hometamon\n')}
        print(result.json)
        self.assertEqual(result.json, doc)

if __name__ == "__main__":
    unittest.main()

import os, sys
import pytest
import textwrap
import falcon
from falcon import testing
import json

sys.path.insert(0, os.path.dirname(__file__))

from src import server

API_KEY = "test"

@pytest.fixture(scope="function")
def app(mocker):
    app = server.create_app(API_KEY)
    return app


def test_sort_libraries():
    message = ""
    expected = ""
    assert server.sort_libraries(message) == expected

    message = textwrap.dedent(
        """\
        # encoding: utf-8
        import hometamon
        import numpy as np
        import json
        import os, sys
        import cv2
        """
    )
    expected = textwrap.dedent(
        """\
        # encoding: utf-8
        import json
        import os
        import sys\n
        import cv2
        import numpy as np\n
        import hometamon"""
    )
    assert server.sort_libraries(message) == expected


def test_sort_libraries_byname():
    """
    .isort.cfg
    length_sort = False
    librariesが長さ順じゃなくて名前順になるように変更
    """
    message = textwrap.dedent(
        """\
        import a
        import z
        import az"""
    )
    expected = textwrap.dedent(
        """\
        import a
        import az
        import z"""
    )
    assert server.sort_libraries(message) == expected


def test_sort_add_byhand():
    message = textwrap.dedent(
        """\
        import a
        import z
        import az"""
    )
    expected = textwrap.dedent(
        """\
        import a
        import az
        import z"""
    )


@pytest.fixture()
def app():
    return testing.TestClient(server.create_app(API_KEY))


def test_get_message(app):
    expected = {"message": "Hello Pisort"}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    result = app.simulate_get("/", headers=headers)
    assert result.json == expected


def test_post_message(app):
    body = {"message": "return same text"}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    result = app.simulate_post("/", body=json.dumps(body), headers=headers)
    expected = {"message": "return same text"}
    assert result.json == expected
    assert result.status == "200 OK"


def test_post_message_wrong_endpoint(app):
    body = {"message": "return same text"}
    headers = {"Content-Type": "application/json"}
    result = app.simulate_post("/src/", body=json.dumps(body), headers=headers)
    assert result.status == "404 Not Found"


def test_posr_sort(app):
    body = {
        "message": (
            textwrap.dedent(
                """\
            # encoding: utf-8
            import hometamon
            import numpy as np
            import json
            import os, sys
            import cv2"""
            )
        )
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    result = app.simulate_post("/", body=json.dumps(body), headers=headers)
    doc = {
        "message": (
            textwrap.dedent(
                """\
            # encoding: utf-8
            import json
            import os
            import sys

            import cv2
            import numpy as np

            import hometamon"""
            )
        )
    }
    assert result.json == doc
    assert result.status == "200 OK"


def test_post_null(app):
    body = {"message": ()}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    result = app.simulate_post("/", body=json.dumps(body), headers=headers)
    doc = {"message": ("")}
    assert result.json == doc
    assert result.status == "200 OK"


def test_unauthorize(app):
    body = {}
    result = app.simulate_post("/", body=json.dumps(body))
    assert result.status == "401 Unauthorized"

def test_post_bad_request(app):
    body = {}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    result = app.simulate_post("/", body=json.dumps(body), headers=headers)
    assert result.status == "400 Bad Request"

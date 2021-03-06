from http import HTTPStatus
from unittest.mock import patch

from sqllineage.drawing import app


@patch("flask.Flask.run")
def test_flask_handler(_):
    option = {"e": "select * from dual", "p": 5000}
    with app.test_client() as c:
        c.get("/")
        resp = c.post("/lineage", json=option)
        assert resp.status_code == HTTPStatus.OK

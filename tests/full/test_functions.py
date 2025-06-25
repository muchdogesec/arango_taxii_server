from arango_taxii_server.app.views import noop_filter


def test_noop_filter():
    assert noop_filter(None, [1,2,3]) == [1,2,3]
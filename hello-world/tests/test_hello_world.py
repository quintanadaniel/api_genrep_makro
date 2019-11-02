import pytest

import hello_world


@pytest.mark.parametrize("a,b", (
    (1, 2),
    (3, 4),
))
def test_thing(a, b):
    assert a
    assert b


def test_blank():
    assert hello_world


def test_with_fixture(fixture_name):
    assert fixture_name

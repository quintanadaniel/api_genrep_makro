import pytest

import generadorDeReportes


@pytest.mark.parametrize("a,b", (
    (1, 2),
    (3, 4),
))
def test_thing(a, b):
    assert a
    assert b


def test_blank():
    assert generadorDeReportes


def test_with_fixture(fixture_name):
    assert fixture_name

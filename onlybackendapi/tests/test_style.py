import os

from flake8.main.application import Application
import pytest


@pytest.mark.parametrize("dir", (
    'generadorDeReportes',
    'tests',
))
def test_flake8(dir):
    src_dir = os.path.abspath(os.path.join(__file__, '..', '..', dir))
    app = Application()
    app.run([src_dir])
    assert app.result_count == 0

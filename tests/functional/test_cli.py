import io

import pytest


from distro.distro import main


@pytest.fixture
def stdout():
    return io.StringIO()


def test_empty_search(stdout):
    raise NotImplementedError


def test_single_term_no_result(stdout):
    raise NotImplementedError


def test_version(stdout):
    raise NotImplementedError


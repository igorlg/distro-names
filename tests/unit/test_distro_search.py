import pytest

from distro.distro import load, search


@pytest.fixture()
def distros():
    return load()


def test_empty_search(distros):
    raise NotImplementedError


def test_single_term_no_result(distros):
    raise NotImplementedError


def test_single_term_one_result(distros):
    raise NotImplementedError


def test_single_term_multiple_results(distros):
    raise NotImplementedError


def test_two_terms_no_result(distros):
    raise NotImplementedError


def test_two_terms_one_result(distros):
    raise NotImplementedError


def test_two_terms_multiple_results(distros):
    raise NotImplementedError


def test_output_text(distros):
    search(['xxx'], distros)
    raise NotImplementedError


def test_output_csv(distros):
    search(['xxx'], distros)
    raise NotImplementedError


def test_output_json(distros):
    search(['xxx'], distros)
    raise NotImplementedError

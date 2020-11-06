import pytest

from distro.distro import load


@pytest.fixture()
def distros():
    return load()


def test_name_required(distros):
    raise NotImplementedError


def test_version_or_versions_required(distros):
    raise NotImplementedError


def test_versions_list(distros):
    raise NotImplementedError


def test_version_absent(distros):
    raise NotImplementedError


def test_default_flavour(distros):
    raise NotImplementedError


def test_extra_args(distros):
    raise NotImplementedError


def test_setup_from_dict(distros):
    raise NotImplementedError


def test_setup_from_args(distros):
    raise NotImplementedError


def test_output_str(distros):
    raise NotImplementedError


def test_output_raw(distros):
    raise NotImplementedError

import pytest

from el_generale import __version__
from el_generale.noneptr import Noneptr


def test_version():
    assert __version__ == '0.1.0'


def test_is_not():
    assert not Noneptr


def test_type_is_none():
    assert isinstance(type(Noneptr), type(None))


def test_call_is_none():
    assert Noneptr() is None


@pytest.mark.skip(reason="It's still not None, PyObject-wise; until I find the way to make those 'synonyms'...")
def test_is_none():
    assert Noneptr is None


def test_is_singleton():
    from el_generale.noneptr import _Noneptr
    another_instance = _Noneptr()
    assert Noneptr is another_instance

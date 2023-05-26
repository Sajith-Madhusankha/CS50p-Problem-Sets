import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("0/2") == 0
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_xlarge():
    with pytest.raises(ValueError):
        convert("2/1")
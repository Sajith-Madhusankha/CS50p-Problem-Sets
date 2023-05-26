from twttr import shorten

def test_shorten_text():
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"


def test_shorten_empty():
    assert shorten("") == ""


def test_shorten_numbers():
    assert shorten("1234") == "1234"


def test_shorten_characters():
    assert shorten("!@#$~Hello WoRLd") == "!@#$~Hll WRLd"
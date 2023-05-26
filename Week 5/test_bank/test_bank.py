from bank import value


def test_value_hello():
    assert value("hello") == 0


def test_value_hstart():
    assert value("how are you?") == 20


def test_value_case():
    assert value("HoW aRe You?") == 20


def test_value_otherwise():
    assert value("Whats up!") == 100